import pandas as pd
import io
import matplotlib.pyplot as plt

s = ""
line = True
with open("./nohup.out", encoding="utf8", mode="r") as f:
    lines = f.read().split("\n")
for line in lines:
    if "[TRAIN]" in line:
        s += (
            line.replace("[TRAIN] Iter: ", "")
            .replace("Loss: ", "")
            .replace(" PSNR: ", "")
        )
        s += "\n"

df = pd.read_csv(io.StringIO(s), delimiter=" ", header=None)
df.columns = ["epoch", "loss", "psnr"]

fig, ax = plt.subplots(figsize=(20, 5))
ax_t = ax.twinx()

ax.plot(df.epoch, df.loss, label="loss", color="r")
ax_t.plot(df.epoch, df.psnr, label="PSNR", color="b")

ax.legend()
ax_t.legend()
ax.set_title("NERF train")
fig.savefig("./nerf.png")
