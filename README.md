# heipy

### requirements

```
pip install Jpype1
```

### setup

1. Install treetagger  
```
cd libs/treetagger
bash download.sh
bash install-tagger.sh
```

2. Set the treeTaggerHome value in the config.props file  
You must set the absolute path of the `libs/treetagger` directory on line 24 of the `libs/config.props` file.