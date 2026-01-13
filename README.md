# Argon Fan HAT Home-Assistant Addon

<https://argon40.com/en-gb/products/argon-fan-hat>

Home Assistant (HASS) Addon to support the Argon Fan HAT

This is a copy of fork of tgryphon's fork for a Waveshare PWM Fan HAT, which fixed problems with reschix's original which started to throw errors after July 2023. There is not much of the original code remaining but credit where it's due, a lot of the problems I'd have had with getting started with a HASS addon had already been solved by them.

See the [DOCS](./DOCS.md) page for details of how to install and use this add-on.

## Development

Push changes to this repo with a bumped version in config.yaml and in main.py, then refresh the add-ons in Home Assistant and an updated version numbber should appear. I don't know if it's mandatory to bump the version number to pull new changes in Home Assistant but it helps with debugging.

## Support

There isn't any support for this plugin. I have two kids and next to no free time, you are welcome to raise PRs but I can't promise if I'll ever get to them. If you want to make any changes you're best off forking this repo and making them yourself. Good luck!
