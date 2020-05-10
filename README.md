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

A full working example with a web-site with a pop-up:

```bash
docker-compose run screenshot \
  --output=example.png \
  --log=debug \
  --pop-up="/html/body/tommi-topper/tt-tmv/div[4]/div[1]/button[2]" \
  "https://topomapviewer.ngi.be/?l=en&x=673574.21&y=674008.07&zoom=8&baseLayer=ngi.cartoweb.topo.be"
```

## Useful websites

- [Lantemätariet](https://kso.etjanster.lantmateriet.se/) for Sweden.
- [Het Nationaal Geografisch Instituut](https://topomapviewer.ngi.be/) for
  Belgium.
- [Jāņa sēta](https://my.balticmaps.eu/) for Latvia.
- [Latvijas Ģeotelpiskās informācijas aģentūra](https://kartes.lgia.gov.lv/) for
  Latvia.
