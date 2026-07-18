# ADR (Architecture Decision Record): HR Handbook Assistant

| Field | Value |
| **Status** | Accepted |
| **Date** | 2026-07-17 |
| **Deciders** | AI Platform Team |

## Context

We need an AI assistant that answers employee questions from a 300 page HR handbook. The handbook is revised roughly once per quarter and every answer must cite the specific source paragraph it was drawn from, so employees and HR staff can verify policy text directly.

## Decision

We will use Retrieval Augmented Generation (RAG): chunk the handbook into paragraph-level passages, embed and index them in a vector store, retrieve the top relevant passages for each query and have the model generate an answer grounded in those passages with citations back to the source paragraph.

## Inputs

- Employee's question, submitted through chat.
- The current quarter's indexed handbook passages.
- Optional conversation context from earlier turns in the same session, for follow-up questions.

## Tools

- Vector search / retriever over the indexed handbook (semantic similarity search).
- Embedding model used to index passages and encode incoming queries.
- Citation formatter that maps a retrieved chunk back to its source paragraph, section, and page number.

## Memory

- No long-term memory of individual employees or past questions is retained.
- Short-term session context only, to support follow-up questions within one conversation.


## Outputs

- A natural-language answer grounded in the retrieved passages.
- An inline citation to the specific source paragraph(s), including section and page reference.
- A fallback "not covered in the handbook" response will be displayed when no passage meets the relevance.

## Autonomy

Low autonomy. The assistant only retrieves and answers — it does not take actions on the employee's behalf.

## Success Metrics

- **Citation accuracy**: percentage of answers whose cited paragraph actually supports the claim made.
- **Employee satisfaction**: thumbs-up rate or survey score on answer helpfulness.
- **Escalation rate**: share of queries employees still had to route to HR after using the assistant.

## Rationale

RAG best fits the requirements for three reasons:

- **Citability**: retrieval returns the exact source chunk, so answers can cite the specific paragraph.
- **Freshness**: the handbook changes quarterly. Re-indexing updated passages is fast and cheap; fine-tuning would require retraining after every revision.
- **Cost and scale**: a 300-page document is too large to paste into every prompt; retrieval keeps each request small and focused on only the relevant passages.

