# VSCode settings.json configuration

Add the following code to .vscode/settings.json to configure black

```sh
{
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": [
    "--line-length",
    "88"
  ],
  "[python]": {
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
}
```
