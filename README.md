<table align="center">
  <tr>
    <td><img src="./images/meta_logo.png" width="200px" /></td>
    <td><img src="./images/huggingface_logo.png" width="200px" /></td>
  </tr>
</table>

# BlogGPT: LLama 3 fine-tuned for writing food and travel blogs
***

[**Overview**](#1)
| [**Download**](#2)
| [**Blog**](#3)
| [**Notable**](#4)
<div id='1'></div>

## Overview
***
BlogGPT writes your first draft! You give it your blog title and headings, and it does the rest!


Under the hood, BlogGPT is powered by a fine-tuned version of LLama 3 8B Instruct.

TRY IT OUT!  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wW-QVKf4MEVFzFIxRH18va2iZWYK4kts?usp=sharing)
<br>
<div id='2'></div>

## Download
***
To download, clone my repo!

```bash
git clone https://github.com/codyfalkosky/BlogGPT.git
```

<br>
<div id='3'></div>

## Blog
***

Writing a food/travel blog is easy!


```python
from BlogGPT import BlogGPT

# init BlogGPT
blog_GPT = BlogGPT()

# set generation parameters title and headings

# title is a single string
title = 'Best Restaurants in LA'

# headings is a list of strings with appropriate level h tags
headings=['<h1>Best Restaurants in LA</h1>', 
            '<h2>Wurstkuche</h2>',
                '<h3>Fries</h3>',
                '<h3>Beer</h3>',
                '<h3>Sausage</h3>',
            '<h2>Bottega Louie</h2>',
                '<h3>Pizza</h3>',
                '<h3>Dessert</h3>',
                '<h3>Breakfast</h3>',
            '<h2>Cut</h2>', 
                '<h3>Meat</h3>',
                '<h3>Wine</h3>',
            '<h2>Tacos Guelaguetza</h2>',
                '<h3>Tacos</h3>',
            '<h2>Conclusion</h2>']

# blog_GPT
blog_GPT.blog(title, headings)
```


<br>
<div id='4'></div>

## Notable
***

### Data Preparation
The data collection and cleaning process was by far the greatest challenge of this project.  First, the website data was downloaded, then the articles were extracted from the HTML.  Then the title, headings, and content were parsed. Finally, the information was packed into LLama 3 instruction format for fine-tuning.  See the detailed story at the link below.  
[LINK](./Data_Preparation.md)  

### SFTTrainer Subclassing
To my knowledge, the `SFTTraining` class does not support subsampling of the evaluation dataset. This meant that every evaluation loop was done on the entire testing dataset.  I solved this by subclassing the SFTTrainer to add functionality for evaluation dataset sampling.  Check it out!  
[LINK](./SFTTrainer_Subclassing.ipynb)

### Training
The model was trained in Google Colab on an A100 using a modified version of the Unsloth training notebook.  Full notebook below.  
[LINK](https://colab.research.google.com/drive/1nrpi6sL9GWrft0UPe_iJLKEnxwO1jAPD?usp=sharing)

### Choosing the Final Model
Loss, checkpoints and choosing the final model.  
[LINK](./Choosing_The_Final_Model.md)


