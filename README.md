# First Person Singular Pronoun Analysis
![Alt text](./docs/shields/Python-3.6-blue.svg)

First singular person pronouns have a relevant scientific importance as indicators of depression, anxiety and mental disease. Such a problem can be explored with linguistic analysis, evaluating how much frequently people talk about themselves. Therefore, the attention moves into linguistic indicators, such as the pronouns *I*, *me*, *my* and *mine*.

That framework aims to provide a tool for computing the first person singular pronouns frequency in a pool of samples.


## Microservice

### How to run it
Build an image using the Dockerfile:
```bash
$ docker build -t lcarnevale/first-person-analysis .
```

Run the image, exposing the dev port:
```bash
$ docker run -d --rm -p 5005:5005 --name first-person-analysis lcarnevale/first-person-analysis
```


## Credits
The project is part of the scientific research carried out at [University of Messina](https://www.unime.it/en) and it aims to be a research product.
