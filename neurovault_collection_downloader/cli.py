# -*- coding: utf-8 -*-

"""Console script for neurovault_collection_downloader."""
import sys
import click
import json, requests
import os, errno
import urllib.request, urllib.parse, urllib.error

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def fetch_collection(col_id, destination_folder, alt_label=None):
    images_url_template = "http://neurovault.org/api/collections/%s/images/"
    next_url = images_url_template%col_id
    images = []
    while next_url:
        click.echo("fetching %s"%next_url)
        resp = requests.get(url=next_url)
        data = json.loads(resp.text)
        images += data['results']
        next_url = data['next']

    if alt_label is not None:
        col_folder = os.path.join(destination_folder, alt_label)
    else:
        col_folder = os.path.join(destination_folder, "%s"%col_id)

    mkdir_p(col_folder)
    json.dump(images, open(os.path.join(col_folder, "images.json"), "w"), 
              indent=4, sort_keys=True)
    for image in images:
        click.echo("fetching %s"%image['file'])
        fname = os.path.basename(image['file'])
        print("saving",image['file'],"to",os.path.join(col_folder, fname))
        urllib.request.urlretrieve(image['file'], os.path.join(col_folder, fname))


@click.command()
@click.argument('collection_list_file', nargs=1, type=click.File('r'))
@click.argument('destination_folder', nargs=1, type=click.Path())
def main(collection_list_file, destination_folder):
    for line in collection_list_file:
        col_id = line.strip()
        click.echo(col_id)
        fetch_collection(col_id, destination_folder)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
