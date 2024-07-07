# New UI For Curator

This is my notes on how I would like the new UI to look, so I can put everything down in one place before breaking the work into tickets.

## UI Philosophy
I want the UI to feel similar to users who do some amount of work on the command line already. As such, this way of using the Curator tool is similar in concept to Git. For git, the central collection of files being managed is the "repository." For Curator, it will be the "collection".

For Curator, a collection is a set of resource files (for now, that just means images), together with metadata about those files. Curator facilitates multiple ways to find and add new images to a collection (e.g. searching the internet, importing images from an existing directory structure, etc.). A single installation of Curator can facilitate working with multiple collections, but each collection is independent of the others. For now all of those collections will be local to the machine running Curator, but in the future we may support cloud-based collections.

A typical workflow for building a collection would first involve initializing a new collection, adding images to it from various sources, and then exporting a dataset for use in machine learning. The dataset can be exported as a CSV file, or as a new directory structured to convey the metadata about the images in a way that is easy to use with machine learning libraries.

The application is intended to be installed using pipx:
```bash
pipx install data-curator
```

## UI Components
TODO

## UI Workflow

### Example 1
This workflow creates a new collection, imports images from an existing directory, then augments the data with several manual searches from the internet. It then exports a dataset as a directory structure.

1. User initializes a new collection
The command below will create a new collection in the current directory with the name "dogs-and-cats". The name option is not required, but it is recommended to give the collection a name that is descriptive of its contents. This allows curator to easily reference the collection for other commands without having to specify the full file path or other collection information.
```bash
cd /path/to/collections/collection_1
curator init . --name "dogs-and-cats"
```

2. User imports images from an existing directory
The command below will import all images from the directory `/path/to/dogs` into the collection. The `--tag` option will tag all images with the tag "dog". The --tag-with-parent-directory option will also tag each image with the name of the parent directory of the image file (useful for example if the images are already organized into sub-directories based on their label).
```bash
curator import directory /path/to/dogs --tag "dog" --tag-with-parent-directory
```

3. User searches the internet for more images
```bash
curator import search --term "American Shorthair" --tag "cat" --tag "shorthair"
curator import search --term "Persian Longhair" --tag "cat" --tag "longhair"
curator import search --term "Cat Breed Siamese" --tag "cat" --tag "shorthair"
```

4. User exports a dataset
The default output format for a dataset is a directory structure with its root at the path specified by `--output`, and a sub directory for each label specified by `--labels`. The images in each sub-directory will be symbolic links to the images in the collection that have that label. 
```bash
curator export dataset --labels dog cat --output /path/to/output
```

### Example 2
In this example, the user creates a new collection and then imports images from several internet searches that they have specified in a file. Then they export a dataset as a CSV file, using both images from this collection as well as from the named collection from example 1.

1. User initializes a new collection
```bash
cd /path/to/collections/collection_2
curator init . --name "birds"
```

2. User imports images from a shopping list
The shopping list as a YAML file placed in the root directory of the collection. The file should have the following format:
```yaml
searches:
    - term: "American Robin"
        tags: ["bird", "robin"]
    - term: "American Goldfinch"
        tags: ["bird", "goldfinch"]
    - term: "American Bald Eagle"
        tags: ["bird", "eagle"]
```

The user can then import images from the shopping list using the `curator import search` command. If this comand is not given specific search terms using the `--term` option, it will instead look for a shopping list and execute the searches specified there.
```bash
curator import search
```

3. User exports a dataset
Note that you can include more than one collection in the creation of a dataset by using the `--include-collections` option. This will include all images from the primary collection, plus any named collections specified in the option.
```bash
curator export dataset \
  --label bird cat \
  --format csv \
  --include-collections dogs-and-cats \
  --output /path/to/output/birds-and-cats-dataset.csv
```