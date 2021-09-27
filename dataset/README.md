# Dataset of Unsafe jQuery Method Calls

To evaluate abilities of [our jQuery XSS Static Analyser](../README.md) and
to compare it with other tools, we created this dataset. It consists of nearly
400 different samples of code and focuses on unsafe jQuery method calls.
Samples are divided into two groups:

1) Context Awareness,
2) Taint & Data Flow Analysis.

The first group of samples includes code with various contexts, therefore
trivial tools without context-aware parsers are eliminated from comparison.
The second group includes code where ability to perform taint analysis and
data flow analysis is required. This means the tool must understand whether
and how are malicious data sanitized on paths from *sources* to vulnerable
*sinks*; also how are these *sources* & *sinks* propagated through expressions.

We compare our tool with [ESLint](https://eslint.org/) and also
[ESLint with *jquery-unsafe* plugin](https://github.com/cdd/eslint-plugin-jquery-unsafe).
**For results of the evaluation of tools and discussion,
please see [our paper](../README.md#publication).**

The dataset is a combination of static code samples and code samples
generated from templates for each analyzed unsafe jQuery method.
Full dataset can be generated with `generate.sh` script. 
[Our jQuery XSS Static Analyser](../README.md) and
[ESLint with *jquery-unsafe* plugin](https://github.com/cdd/eslint-plugin-jquery-unsafe)
can be tested with the dataset using `test.sh` script
and `preview.sh` script helps with examining test results.
The whole procedure can be following:

```shell
npm install
python -m pip install -r requirements.txt
./generate.sh
./test.sh
./preview.sh
```
