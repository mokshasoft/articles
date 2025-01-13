# Proposal: Training LLMs Without Additional Data

I propose a method for training large language models (LLMs) without requiring additional data. This idea emerged during a discussion with ChatGPT, where, after several back-and-forth exchanges, the model changed its stance on a particular question. Importantly, the reasoning it used relied entirely on existing knowledge—it didn’t require new data to grasp the concept. Instead, it distilled or extracted insights from its current dataset. This process mirrors how humans often learn and might provide a way to improve LLMs without introducing more data.

Currently, training LLMs involves vast amounts of data, much of which contains inaccuracies, biases, and misleading or unbalanced information. While one approach to improving LLMs is to curate higher-quality training data, I suggest an alternative: using an agentic setup to extract and refine knowledge from the existing dataset, akin to the scientific process.

In this setup, two LLMs could take opposing sides on a topic and engage in a structured debate. A third LLM would then evaluate the arguments and determine which side presents the most logical and compelling case. This iterative process would adjust the weights of the models to favor logical and well-reasoned answers. This approach is promising because evaluating the coherence of arguments is often easier than generating them or uncovering novel insights in raw data.

The following discussion with ChatGPT provides an example of this process in action:
https://chatgpt.com/share/6784d9fe-9590-8001-b7ca-36120fd25b64

Given the abundance of available data, this process could likely run indefinitely, continuously improving model performance—just as humanity’s collective knowledge grows over time.
