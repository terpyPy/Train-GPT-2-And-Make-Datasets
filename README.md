# This is the merging of OpenAI's GPT-2 Repository and the Train your own repo from nsheaperd, i am in no way affiliated with eaither of them!!!!!!!!!!!!
I made this repo to train gpt-2 on rap lyrics and lovecrafts books, 
when i started there was no one repository with the tranng scripts up to date with the model downloads
also the prev training repo used none exsitient 117m Models

# python enviorment 3.5.4 or lower is needed as tensorflow 1.12.0 fully deprecatied with tensorflow 2 release.
use conda or your own env methoid, if you dont know how google it, time to learn.....
or just use the docker files which will set this up in a VM with proper version.

# What I added
i added the scripts to help make some basic large text files,
1. get_tweets.py: if you get twitter api access use this to download all of someones tweets
2. playlistV2.py: has a UI that operates youtube-dl cmd arguments, lets you download the auto-genarated subtitles form any video

# Data set tools uses
get_tweets requires a twitter dev account for api accesse,
modify these variables:
	consumer_key = ""
	consumer_secret = ""
	access_key = ""
	access_secret = ""
	

this script writes a csv file with last 100 tweets to do more modifiy:
	number_of_tweets = 100
if you want audio transcripts to train on podcast text run playlistV2:
1. fill in a url in the text field on top
2. click the "auto gen subtitles button"
3. click download playlist

if you wanna download the video as well just click add url again and click download.
if you mess up the like just click reset.

# video of output from my models:
https://www.youtube.com/watch?v=5G_YIbovFsQ&ab_channel=Terpy

# gpt-2 (OpenAI's readme keeping for beravity, I DO NOT OWN THIS NOR CLAIM ANY OF THERE WORK)

Code and models from the paper ["Language Models are Unsupervised Multitask Learners"](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf).

You can read about GPT-2 and its staged release in our [original blog post](https://blog.openai.com/better-language-models/), [6 month follow-up post](https://openai.com/blog/gpt-2-6-month-follow-up/), and [final post](https://www.openai.com/blog/gpt-2-1-5b-release/).

We have also [released a dataset](https://github.com/openai/gpt-2-output-dataset) for researchers to study their behaviors.

<sup>*</sup> *Note that our original parameter counts were wrong due to an error (in our previous blog posts and paper).  Thus you may have seen small referred to as 117M and medium referred to as 345M.*

## Usage

This repository is meant to be a starting point for researchers and engineers to experiment with GPT-2.

For basic information, see our [model card](./model_card.md).

### Some caveats

- GPT-2 models' robustness and worst case behaviors are not well-understood.  As with any machine-learned model, carefully evaluate GPT-2 for your use case, especially if used without fine-tuning or in safety-critical applications where reliability is important.
- The dataset our GPT-2 models were trained on contains many texts with [biases](https://twitter.com/TomerUllman/status/1101485289720242177) and factual inaccuracies, and thus GPT-2 models are likely to be biased and inaccurate as well.
- To avoid having samples mistaken as human-written, we recommend clearly labeling samples as synthetic before wide dissemination.  Our models are often incoherent or inaccurate in subtle ways, which takes more than a quick read for a human to notice.

### Work with us

Please [let us know](mailto:languagequestions@openai.com) if you’re doing interesting research with or working on applications of GPT-2!  We’re especially interested in hearing from and potentially working with those who are studying
- Potential malicious use cases and defenses against them (e.g. the detectability of synthetic text)
- The extent of problematic content (e.g. bias) being baked into the models and effective mitigations

## Development

See [DEVELOPERS.md](./DEVELOPERS.md)

## Contributors

See [CONTRIBUTORS.md](./CONTRIBUTORS.md)

## Citation

Please use the following bibtex entry:
```
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
```
