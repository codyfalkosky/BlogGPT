<div align="center">
    <img src="./images/meta_logo_pad.png" width="200px"></img>
    <img src="./images/huggingface_logo.png" width="200px"></img>
</div>

# BlogGPT: Data Preparation
***

[**Data Collection**](#1)
| [**Article Extraction**](#2)
| [**Article Parse**](#3)
| [**Conversion to Message Format**](#4)
| [**Next Steps**](#5)
<div id='1'></div>

## Data Collection
***
I located 27 websites with many blog posts and used wget to download and build a local tree of each website and all its contents to make the article extraction process local, repeatable and tweakable.  The scraping process took about 1 day.

<div id='2'></div>

## Article Extraction
***

With all data local, the next challenge was to extract each blog from its raw HTML.  I first created a base class that could iterate through articles, save the data, and parse simply.  Then, for each new website, I customized the parsing portion of the class to fit the individual file tree and HTML style of the specific website and file tree.  To see the exact process, check out this link below.

[NOTEBOOK](Data_Prep_Notebooks/1_Extract_Article.ipynb)

<div id='3'></div>

## Article Parse
***

Now, with the article extracted from the HTML, the title, headings, and content related to the headings had to be parsed to conform to the desired function of the final product.  This was done similarly to the previous, building a base class and tweaking it for each individual HTML formatting style.  This information was parsed from the HTML and saved into a JSON file.

[NOTEBOOK](Data_Prep_Notebooks/2_Parse_Article.ipynb)

<div id='4'></div>

## Conversion to Message Format
***

Given the intention to fine-tune the LLama 3 Instruct model, the training data needed to conform to the specific message format required by LLama 3 Instruct.  Multiple prompts were generated and labeled, then saved into a list in a JSON file containing approximately 15k blog generation examples.

[NOTEBOOK](Data_Prep_Notebooks/3_Convert_To_Message.ipynb)

<div id='5'></div>

## Next Steps
***

Now we have a JSON file containing a list of dictionaries with keys 'messages' containing the prompt and desired response and 'label' notating the type of prompt.  We are ready to train!

[Training Colab Link](https://colab.research.google.com/drive/1nrpi6sL9GWrft0UPe_iJLKEnxwO1jAPD?usp=sharing)
