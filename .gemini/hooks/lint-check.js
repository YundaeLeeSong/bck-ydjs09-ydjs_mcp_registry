const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

function run() {
    const pkgPath = path.resolve(process.cwd(), 'package.json');
    
    // 1. Check if package.json exists, initialize if not
    if (!fs.existsSync(pkgPath)) {
        console.log("No package.json found. Initializing...");
        execSync('npm init -y', { stdio: 'ignore' });
    }

    // 2. Check if eslint is installed
    let pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
    
    if (!pkg.devDependencies || !pkg.devDependencies.eslint) {
        console.log("Installing ESLint as a devDependency (this might take a few seconds)...");
        // Install eslint silently
        execSync('npm install --save-dev eslint --silent', { stdio: 'ignore' });
        
        // Reload package.json after install
        pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
    }

    // Ensure lint:quiet script exists and is mapped to eslint
    const isDummy = pkg.scripts && pkg.scripts['lint:quiet'] === "echo \"Linting passed (dummy)\"";
    const isMissing = !pkg.scripts || !pkg.scripts['lint:quiet'];
    
    if (isDummy || isMissing) {
        pkg.scripts = pkg.scripts || {};
        pkg.scripts['lint:quiet'] = "eslint . --quiet";
        fs.writeFileSync(pkgPath, JSON.stringify(pkg, null, 2));
    }

    // NEW: Ensure a basic eslint config exists (v9/v10 flat config)
    // Using CommonJS for the config to be most compatible with various node setups
    const configPath = path.resolve(process.cwd(), 'eslint.config.js');
    const configMjsPath = path.resolve(process.cwd(), 'eslint.config.mjs');
    const configCjsPath = path.resolve(process.cwd(), 'eslint.config.cjs');

    if (!fs.existsSync(configPath) && !fs.existsSync(configMjsPath) && !fs.existsSync(configCjsPath)) {
        console.log("No ESLint config found. Creating default eslint.config.js...");
        // Bare minimum flat config that doesn't require @eslint/js to be installed
        const defaultConfig = `module.exports = [
    {
        ignores: [".gemini/**"]
    },
    {
        files: ["**/*.js"],
        languageOptions: {
            ecmaVersion: "latest",
            sourceType: "commonjs",
            globals: {
                console: "readonly",
                process: "readonly",
                module: "readonly",
                require: "readonly",
                __dirname: "readonly"
            }
        },
        rules: {
            "no-unused-vars": "error",
            "no-undef": "error"
        }
    }
];\n`;
        fs.writeFileSync(configPath, defaultConfig);
    }

    // 3. Try running npm run lint:quiet
    try {
        const output = execSync('npm run lint:quiet --silent', { encoding: 'utf-8', stdio: ['ignore', 'pipe', 'pipe'] });
        if (output && output.trim()) {
            console.log(output.trim());
        } else {
            console.log("Linting passed.");
        }
    } catch (e) {
        // Execution throws if the lint command exits with a non-zero code (meaning linting errors were found)
        if (e.stdout) console.log(e.stdout.trim());
        if (e.stderr) console.log(e.stderr.trim());
        
        if (!e.stdout && !e.stderr) {
            console.log("Failed to run lint command. Error: " + e.message);
        }
    }
}

try {
    run();
} catch (err) {
    console.error("Hook error:", err.message);
}
