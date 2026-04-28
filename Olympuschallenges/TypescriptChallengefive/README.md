Repository
https://github.com/rcaferati/react-awesome-slider
Commit: 09a811b8f4a62d90b52664ab2dd06727c83a3265

Title
Autoplay with per-slide duration and direction control

`AwesomeSlider` needs support for automatic slide advancement. When `autoplay` is enabled the slider cycles through slides on its own. The global dwell time is controlled by `autoplayInterval` (default 3000ms). `autoplaySpeed` divides the interval to produce the effective dwell time; the result is rounded to the nearest integer millisecond and clamped to a minimum of 50ms. Invalid speed values - zero, negative, NaN, or Infinity - fall back to 1. `autoplayDirection` accepts "next" (default) or "prev".
Individual slides can set a `duration` field in milliseconds to override the global interval for that slide. Zero, negative, and NaN values fall back to `autoplayInterval`. Infinity is accepted as a positive override but normalizes to the 50ms minimum after speed scaling.
Autoplay does not start until the slider has fully started; when `startupScreen` is provided and `startup={false}`, the slider remains in its startup phase and autoplay is suppressed until started. During the startup phase the Bullets component is not rendered. `pauseOnHover` pauses on mouse-enter and resumes on mouse-leave, unless `pause()` was called explicitly - in that case mouse-leave must not resume cycling. `pause()` and `play()` are exposed on the component ref; calling `play()` while already playing is idempotent. `onTransitionStart` and `onTransitionEnd` fire for autoplay-triggered navigation as well as manual navigation.
When `infinite` is false autoplay stops at the terminal slide; when true (the default) it wraps. A `disabled` slider or one with a single slide suppresses autoplay. Any arrow or bullet click cancels the pending timer and reschedules it using the incoming slide's effective dwell time.
The slider renders an element with the class `awssld__wrapper` that is the intended target for `mouseenter`/`mouseleave` events used by `pauseOnHover`.
The Bullets component receives an `onClick` prop with the signature `({ index: number, direction: boolean })`, where `direction` is `true` when navigating forward and `false` when navigating backward. This is a stable public prop contract.
he currently active slide index is tracked via the `selected` prop passed to the Bullets component. Tests infer the active index by reading this value from the rendered bullets element.
