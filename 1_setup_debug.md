# Setting Up Debugging in VS Code

## Task 1.1 Create a debug configuration

1. Open the 'Run and Debug' view (left sidebar) → 'create a launch.json file' → choose 'Python Debugger (Suggested)' → choose 'Python File' → choose 'Python: Current File'.
2. VS Code creates `.vscode/launch.json`. Add the following configuration to it:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

This configuration allows you to run and debug the currently active Python file.