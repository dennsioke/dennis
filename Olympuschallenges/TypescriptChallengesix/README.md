Repository
https://github.com/cloudflare/capnweb
Commit: cfa1b959ebf4cf24c3ea8277f424118306ffff2e

Title
AbortSignal-driven RPC call cancellation with pipeline cascade

RPC promises should be cancellable. A cancel method rejects the promise with a DOMException whose name is "AbortError" and returns void; the message is derived from the provided reason by stringifying it (so passing an Error yields its toString()), and omitting a reason uses a sensible default. A withAbortSignal method wires cancellation to an external AbortSignal and returns the same promise for chaining. If the signal is already aborted at the time withAbortSignal is called, cancellation must happen synchronously.
Cancelling a promise sends a JSON-encoded ["cancel", exportId] message to the peer, where exportId is the numeric identifier of the remote export. The peer disposes the corresponding export on receipt; receiving cancel for an already-disposed or nonexistent export is silently ignored. Cancel is idempotent -- multiple cancel calls or multiple stubs sharing the same underlying import produce exactly one cancel message. When a cancelled promise has pipelined calls hanging off it, those dependents are cancelled recursively through the whole chain, with one cancel message per affected import that has been established on the wire. Cancellation on an already-resolved or disposed promise is a no-op.
