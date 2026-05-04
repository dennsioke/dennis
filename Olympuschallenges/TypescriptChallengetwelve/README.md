Repository
https://github.com/ollama/ollama-js
Commit: 9c92b18d4026f5345ff7950f15216372b23401a1

Title
Automatic retry with exponential backoff for transient failures

It would be useful if the client supported a `retries` config option that automatically retries requests when the server responds with a transient error (429, 502, 503, or 504), rather than throwing immediately.
The wait between attempts should grow exponentially starting at 1000 ms and doubling on each subsequent retry (i.e. 1000 ms, 2000 ms, 4000 ms, …), capped at 30000 ms, so that repeated failures back off gracefully.
Both streaming and non-streaming requests should be retried before any response body is consumed, and if the instance is aborted mid-backoff the pending retry should be cancelled and the request should reject.
Once all retries are exhausted the last error should propagate to the caller.
