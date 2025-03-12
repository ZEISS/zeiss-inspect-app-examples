# SettingsAPI

The Settings API provides persistent storage of App related settings.

The API allows reading/writing values into the ZEISS INSPECT application configuration. This configuration is persistent and will survive application restarts. Also, it can be accessed via the application's preferences dialog.

The configuration entries must be defined in the App's `metainfo.json` file. This configuration defines the available keys, the entry types and the entry properties. If the entry type can be represented by some widget, the setting entry will also be present in the application's ‘preferences’ dialog and can be adapted interactively there.

See [Settings API](https://zeiss.github.io/zeiss-inspect-app-api/2025/python_api/python_api.html#gom-api-settings) for details.
