# Map extractor

A script to take screenshots of web sites in larger dimensions than your
physical screen.

## Example usage

Using `docker-compose`:

```bash
docker-compose run screenshot --output=google.png "https://google.com"
```

For more options run

```bash
docker-compose run screenshot --help
```

### Pop ups

Some web sites do not allow accessing their contents without closing a pop-up or
a pop-up might cover part of the screen. This can be solved by providing XPath
of a button that closes such a pop-up to the `--pop-up` argument.

Example without closing a pop-up:

```bash
docker-compose run screenshot \
  --output=example_without_closing_popup.png \
  --log=debug \
  "https://www.google.com/"
```

Example with closing a pop-up first:

```bash
docker-compose run screenshot \
  --output=example_with_closed_popup.png \
  --log=debug \
  --pop-up="//*[@id='cnsd']" \
  "https://www.google.com/"
```

## Useful websites

- [Lantemätariet](https://kso.etjanster.lantmateriet.se/) for maps of Sweden.
- [Het Nationaal Geografisch Instituut](https://topomapviewer.ngi.be/) for maps
  of Belgium.
- [Jāņa sēta](https://my.balticmaps.eu/) for maps of Latvia.
- [Latvijas Ģeotelpiskās informācijas aģentūra](https://kartes.lgia.gov.lv/) for
  maps of Latvia.
- [Norge.no](https://www.norgeskart.no/) for maps of Norway.
