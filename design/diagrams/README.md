# Platform diagrams

The diagrams shown in the Projects section of joshuel.com.br, drawn with draw.io and the AWS
architecture icons. The `.drawio` files are the source: open them in draw.io, edit, then export.

| File | Shows |
|---|---|
| `aws-accounts.drawio` | The six accounts and what each one is for |
| `github.drawio` | A change from pull request to AWS: plan, approve, apply |
| `network.drawio` | One region's network: Cloudflare, load balancer, app containers, NAT |
| `ecs.drawio` | A sale through the ECS services, from the request until it is processed |
| `eks-planned.drawio` | The planned EKS design (not built yet) |

Keep them simple: one idea per diagram, few boxes, short labels, left to right.

## Export for the site

With draw.io Desktop installed, from this folder:

```bash
for f in *.drawio; do
  draw.io --export --format png --scale 2 --border 16 --output "${f%.drawio}@2x.png" "$f"
done
```

Then make the WebP files in `site/img/arch/` (2x as is, 1x at half size, no metadata):

```bash
for f in *@2x.png; do
  n=${f%@2x.png}
  convert "$f" -strip -quality 88 -define webp:method=6 "../../site/img/arch/$n-2x.webp"
  convert "$f" -strip -filter Lanczos -resize 50% -quality 88 -define webp:method=6 "../../site/img/arch/$n-1x.webp"
done
```

Update the `width`/`height` of the `<img>` in `site/index.html` if a diagram changes size.
