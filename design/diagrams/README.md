# Platform diagrams

The diagrams shown in the Projects section of joshuel.com.br, drawn with draw.io and the AWS
architecture icons. The `.drawio` files are the source: open them in draw.io, edit, then export.

| File | Shows |
|---|---|
| `aws-accounts.drawio` | management on top; Security, Shared and Workloads under it |
| `github.drawio` | The organization, OIDC, and the reusable workflows in three lanes: infra, sites, services |
| `network.drawio` | The production VPC in us-east-1: Cloudflare in front, two AZs, public and private subnets with their CIDRs, one NAT, gateway endpoints |
| `ecs.drawio` | An example app (API and worker) active in two regions: the ECS clusters, the replicated data and the standby copies for failover |
| `eks-planned.drawio` | Planned, not built yet: the platform on EKS in two regions, at the infrastructure level: VPC, load balancer, cluster, Karpenter nodes, Argo CD and Argo Rollouts |

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

## Logos

Cloudflare and Argo come from [simple-icons](https://github.com/simple-icons/simple-icons) 13.0.0 (CC0), Karpenter from `website/assets/icons/logo.svg` of `aws/karpenter-provider-aws` v1.0.0. They are embedded in the `.drawio` files as SVG, so the site makes no request for them.
