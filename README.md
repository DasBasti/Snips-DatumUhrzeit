# Snips-Sprüche 🥴
A patter app for Snips.ai

## Installation

**Important:** The following instructions assume that [Snips](https://snips.gitbook.io/documentation/snips-basics) is
already configured and running on your device. [SAM](https://snips.gitbook.io/getting-started/installation) should
also already be set up and connected to your device and your account.

1. In the German [app store](https://console.snips.ai/) add the
app `Verdrehte Sprüche` (by BastiN; [this](https://console.snips.ai/app-editor/bundle_9P346QWA0xE)) to
your *German* assistant.

2. If you already have the same assistant on your platform, update it
(with [Sam](https://snips.gitbook.io/getting-started/installation)) with:
      ```bash
      sam update-assistant
      ```
      
   Otherwise install the assistant on the platform with [Sam](https://snips.gitbook.io/getting-started/installation)
   with the following command to choose it (if you have multiple assistants in your Snips console):
      ```bash
      sam install assistant
      ```
That's it!

## Usage

With this app you can ask Snips for a random funny saying or multiple in a row.

### Example sentences

#### Random Idiom

- *Verdrehe einen Spruch.*
- *Gib mir einen Spruch.*
- [...]

#### Next Idiom

- *Nächster Spruch.*
- *Noch einen.*
- *Immer her damit.*
- *Ja.*
- [...]

#### Stop

- *Halt.*
- *Stop.*
- *Ich kann nicht mehr.*
- *Nein.*
- [...]

## Contribution

Please report errors (you can see them with `sam service log`) and bugs by
opening a [new issue](https://github.com/DasBasti/Snips-Sprueche/issues/new).
You can also write other idioms/quotes/sayings for this skill. Thank you for your contribution.
