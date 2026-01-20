# Waveshare 2 inch LCD Display Home-Assistant Addon

Home Assistant (HASS) Addon to support displaying basic system information on a Waveshare 2 inch LCD display.

This is specifically for this display: <www.waveshare.com/wiki/2inch_LCD_Module>.

Important: This requires SPI enabled to make this work, done using the Sunfounder Pi Config Add-On. See <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository> for details.

See the [DOCS](./DOCS.md) page for details of how to install and use this add-on.

## Building locally with docker

Riun the following command to replicate the build command from within Home Assistant.

```shell
docker buildx build . --tag 4901440b/aarch64-addon-waveshare_lcd_display_add_on:0.0.5 --file Dockerfile --platform linux/arm64 --pull --build-arg BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest --build-arg BUILD_VERSION=0.0.5 --build-arg BUILD_ARCH=aarch64 
```

## Development

Push changes to this repo with a bumped version in config.yaml and in main.py, then refresh the add-ons in Home Assistant and an updated version number should appear. I don't know if it's mandatory to bump the version number to pull new changes in Home Assistant but it helps with debugging.

## Support

There isn't any support for this plugin. I have two kids and next to no free time, you are welcome to raise PRs but I can't promise if I'll ever get to them. If you want to make any changes you're best off forking this repo and making them yourself. Good luck!
