Repository
https://github.com/ollama/ollama-js
Commit: 9c92b18d4026f5345ff7950f15216372b23401a1

Title
Automatic retry with exponential backoff for transient failures

It would be useful if the client supported a `retries` config option that automatically retries requests when the server responds with a transient error (429, 502, 503, or 504), rather than throwing immediately.
The `retries` value represents the number of additional attempts after the initial request (so `retries: 3` allows up to 4 total attempts). When `retries` is omitted or set to 0, no retries are performed and the first failure is thrown immediately.
The wait between attempts should grow exponentially starting at 1000 ms and doubling on each subsequent retry (i.e. 1000 ms, 2000 ms, 4000 ms, ...), capped at 30000 ms, so that repeated failures back off gracefully.
Both streaming and non-streaming requests should be retried before any response body is consumed, and if the instance is aborted mid-backoff the pending retry should be cancelled and the request should reject.
Once all retries are exhausted the last error should propagate to the caller. If the server included an error message in the response body (e.g. `{ "error": "service unavailable" }`), the rejected error's message should include that server-provided string.
