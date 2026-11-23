# Platform diagrams

The diagrams shown in the Projects section of joshuel.com.br, drawn with draw.io and the AWS
architecture icons. The `.drawio` files are the source: open them in draw.io, edit, then export.

| File | Shows |
|---|---|
| `aws-accounts.drawio` | management on top; Security, Shared and Workloads under it |
| `github.drawio` | A change from pull request to AWS: plan, approve, apply |
| `network.drawio` | One region's network: Cloudflare, load balancer, app containers, NAT |
| `ecs.drawio` | A sale through the ECS services, from the request until it is processed |
| `eks-planned.drawio` | The planned EKS design (not built yet) |

Keep them simple: one idea per diagram, few boxes, short labels, left to right.

## Export for the site

The site uses SVG: vector, sharp at any size and zoom. With draw.io Desktop installed, from this
folder, export to a temporary folder:

```bash
mkdir -p /tmp/drawio-svg
for f in *.drawio; do
  draw.io --export --format svg --border 16 --output "/tmp/drawio-svg/${f%.drawio}.svg" "$f"
done
```

Then clean them into `site/img/arch/`:

```bash
python3 -I clean_svg.py /tmp/drawio-svg ../../site/img/arch
```

`clean_svg.py` drops the PNG copies draw.io embeds as a fallback for every label (about 90% of
the file), the external "Text is not SVG" link and the dark-mode colours (the diagrams always sit
on white), and refuses any script or external reference. Update the `width`/`height` of the
`<img>` in `site/index.html` if a diagram changes size (the script prints them).
