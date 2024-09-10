<div align="center">
    <img src="./images/meta_logo_pad.png" width="200px"></img>
    <img src="./images/huggingface_logo.png" width="200px"></img>
</div>

# BlogGPT: Choosing the final model
***

[**Paragraph Length**](#1)
| [**Hallucinations**](#2)
| [**Train/Test Loss**](#3)
| [**Conclusion**](#4)
<div id='1'></div>

## Paragraph Length
***

When comparing LLama 3 instruct to the training data, the paragraph lengths were much shorter than the standard blog.  Though out training training the paragraph length improved.

![Paragraph Length by Train Step](./images/paragraph_length_by_training_step.png)

As you can see, by training step 300, the paragraph length was within the acceptable range of a regular blog.

<br>
<div id='2'></div>

## Hallucinations
***

The number of hallucinations was reduced throughout training.

![Hallucinations by Train Step](./images/hallucinations_by_training_step.png)


Though the hallucinations slightly increased at step 300, the number of output sentences per paragraph doubled.  By this metric, step 300 performed best.

## Train/Test Loss

The lowest testing loss occurs around step 300. The red bars illustrate this, showing the mean of roughly one epoch of testing loss.  Beyond step 350, problematic overfitting begins, with the training loss going down but the testing loss starting to go up.

![Train/Test Loss](./images/model_train_test_loss_by_training_step.png)


## Conclusion

Based on three factors of increasing paragraph length, minimizing hallucinations, and avoiding problematic overfitting, the weights from step 300 are the optimal option and will be chosen the the model.