Repository
https://github.com/rcaferati/react-awesome-slider
Commit: 09a811b8f4a62d90b52664ab2dd06727c83a3265

Title
Autoplay with per-slide duration and direction control

The slider automatically advances through slides at a configurable interval when autoplay is enabled. The advancement direction is configurable — slides can cycle forward or backward. A speed multiplier shortens or lengthens how long each slide is displayed: doubling the speed halves each slide's dwell time, and halving the speed doubles it.

Each slide can declare its own dwell time that overrides the global interval. Only positive durations are respected as per-slide overrides; invalid values (zero, negative, NaN) fall back to the global interval. The final dwell time is always at least 50ms regardless of speed scaling, and is rounded to the nearest millisecond.

When hover-pause is enabled, moving the mouse over the slider pauses the slideshow and moving it away resumes it. If autoplay was paused programmatically, a subsequent mouse-leave does not resume it — the programmatic pause takes precedence.

Autoplay is inactive when the slider is disabled, when only a single slide is present, or before the slider has finished its startup animation. When the slider is configured to not loop, autoplay stops when the first or last slide is reached rather than wrapping around.

The slider exposes `play()` and `pause()` methods through its ref, allowing the autoplay to be started and stopped programmatically without changing the currently visible slide. Calling `play()` repeatedly while already playing has no side effects and does not stack duplicate timers. When a user navigates manually — via arrow buttons or bullet indicators — the pending autoplay timer is cancelled and a new one is scheduled based on the incoming slide's dwell time. Unmounting the slider cleans up all pending timers.
