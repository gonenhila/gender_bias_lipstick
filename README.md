# Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them

This project includes the experiments described in the [paper](https://arxiv.org/pdf/1903.03862.pdf): 

**"Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them"**, Hila Gonen and Yoav Goldberg, NAACL 2019.

Full reimplementation of the experiments is available in "remaining_bias_2016.ipynb" for Bolukbasi's embeddings, and in "remaining_bias_2018.ipynb" for Zhao's embeddings.  

## Prerequisites

* Python 2.7

## Download embeddings

As a first step, download the nondebiased and debiased embeddings into **data/embeddings/** from this [folder](https://drive.google.com/drive/folders/1pXL31TU0LPHw9J9p3BXep0O1p2A_rrDZ?usp=sharing) (8 files):

* orig_w2v: Bolukbasi's embeddings, nodebiased
* hard_debiased_w2v: Bolukbasi's embeddings, debiased
* orig_glove: Zhao's embeddings, nodebiased
* gn_glove: Zhao's embeddings, debiased

These files are the original embeddings but with a preprocessing step (for fast loading, see source/save_embeds.py):

* Embeddings of Bolukbasi et al. (hard_debiased) are taken from [nondebiased](https://code.google.com/archive/p/word2vec/) and [debiased](https://github.com/tolga-b/debiaswe).
* Embeddings of Zhao et al. (gn_glove) are taken from [nondebiased](https://drive.google.com/file/d/1jrbQmpB5ZNH4w54yujeAvNFAfVEG0SuE/view) and [debiased](https://github.com/uclanlp/gn_glove).



## Cite

If you find this project useful, please cite the paper:
```
@inproceedings{GONEN19,
  title={Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them},
  author={Gonen, Hila and Goldberg, Yoav},
  booktitle={Proceedings of NAACL-HLT},
  year={2019}
}
```

## Contact

If you have any questions or suggestions, please contact [Hila Gonen](mailto:hilagnn@gmail.com).

## License

This project is licensed under Apache License - see the [LICENSE](LICENSE) file for details.


