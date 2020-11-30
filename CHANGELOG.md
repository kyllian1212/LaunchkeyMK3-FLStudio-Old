# CHANGELOG

## v1.0.0 - Mixer Mode

### New features
* Mixer mode, allowing you to:
  * See the selected mixer track info & volume/pan settings in the 16x2 characters screen
  * Select tracks in the mixer
  * See peak meters in the 8x2 pad grid, either for 8 tracks, a single track or the master (which can be changed in the settings for this mode)
  * Set pan and volume of each track
  * Mute or solo each track

### Changes
* If an inactive button (which means it has no functionality yet) is pressed, but has no LED to allow visual feedback, the screen will now show "Button currently inactive".

### Bugfixes
* Fixed an issue with the mixer volume & pan tracking (which was delayed and inaccurate)
* Not really a bugfix, but I added a crash handler which can help showing when the program crashes

## v0.0.1 - Initial Release
First release!

### Features
* 'Undo', 'Play', 'Stop', 'Record', 'Pattern/Song Toggle' buttons now functional
* Selected mixer track info & volume/pan settings showing in the 16x2 characters screen

Any kind of functionality for the pads, faders and knobs is currently inexistant, but that'll come soon hopefully.
