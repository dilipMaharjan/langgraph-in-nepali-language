# Workflows

## Prompt Chaining

- Techique in NLP where multiple prompts are sequenced in a fashion that guides a model through a complex task or reasoning process.
- Breaks task into smaller, manageable steps, with each step of building on the previous one.
- Imporves accuracy, coherence and control when working with LLM.

## Parallelization

- Multiple nodes can operate without dependency
- Can start at the same time or at a particular point
- Can merge in the downstream nodes based on functionality

## Routing

- Conditionally determine which node should execute next based on current state/output of a node
- promotes dynamic flow
- conditional logic
- Flexibility

## Orchestrator-Worker

- A central LLM dynamically breaks down tasks
- Delegates them to worker LLMs
- Syntheisizes their results.
- Well-suited for complex tasks where you can't predict the subtasks needed.
- Key difference from parallelization is its flexisbility- subtasks aren't pre-defined but determined by the orchestrator based on the specific input

## Evaluator-Optimizer

- One llm generates a response while another provides feedback
- Effective when there is clear evaluation criteria.
- iterative refinement provides refined value
- Optimizer can be replaced with human as well.
