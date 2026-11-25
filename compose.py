#!/usr/bin/env python3
"""Draw the front page for Wednesday 25 November 2026.

A one-image summary of the day's world news, laid out as a newspaper
front page and rendered entirely with PIL so every letter is exact.
Running it twice produces byte-identical output: no clocks, no random
sources, fixed geometry everywhere.
"""

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024

PAPER = (247, 243, 232)
INK = (20, 22, 28)
MUTED = (92, 90, 82)
RED = (164, 28, 32)
NAVY = (24, 42, 84)
RULE = (20, 22, 28)
PANEL = (255, 253, 246)
PANEL_LINE = (196, 188, 168)
GOLD = (176, 132, 40)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def centered(draw, cx, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text((cx - (box[2] - box[0]) / 2 - box[0], y), text, font=fnt, fill=fill)
    return y + (box[3] - box[1])


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def left_text(draw, x, y, text, fnt, fill, max_width, leading):
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- masthead -------------------------------------------------
    draw.rectangle([0, 0, W, 6], fill=INK)
    centered(draw, W / 2, 18, "THE WORLD IN ONE PAGE", font(SERIF_B, 50), INK)
    draw.rectangle([36, 84, W - 36, 87], fill=RULE)
    draw.rectangle([36, 92, W - 36, 94], fill=RULE)
    centered(
        draw, W / 2, 100,
        "All the day's news, drawn on one page  -  Wednesday edition",
        font(SERIF, 19), MUTED,
    )

    # ---- date band ------------------------------------------------
    draw.rectangle([0, 128, W, 184], fill=RED)
    centered(draw, W / 2, 136, "WEDNESDAY 25 NOVEMBER 2026", font(SANS_B, 40), (255, 255, 255))

    # ---- lead story -----------------------------------------------
    draw.text((36, 196), "TRADE  -  WASHINGTON", font=font(SANS_B, 22), fill=RED)
    lead_lines = ["TARIFF FEARS RETURN:", "ASIA TUMBLES"]
    y = 224
    for line in lead_lines:
        draw.text((36, y), line, font=font(SERIF_B, 72), fill=INK)
        y += 78
    y += 2
    y = left_text(
        draw, 36, y,
        "The Trump administration readies new duties after its probe into "
        "excess factory capacity in 16 trading partners, and chip shares "
        "lead a sell-off from Seoul to Taipei as Monday's AI rally fades.",
        font(SANS, 24), (52, 52, 48), W - 72, 31,
    )

    # ---- number strip ---------------------------------------------
    stats = [
        ("KOSPI", "-5.3%"),
        ("TAIWAN", "-5.1%"),
        ("NIKKEI 225", "-2.9%"),
        ("NVIDIA", "-5.9%"),
    ]
    strip_y = y + 12
    cell_w = (W - 72) / 4
    draw.rectangle([36, strip_y, W - 36, strip_y + 78], fill=NAVY)
    for i, (label, value) in enumerate(stats):
        cx = 36 + cell_w * i + cell_w / 2
        centered(draw, cx, strip_y + 8, label, font(SANS_B, 19), (196, 208, 235))
        centered(draw, cx, strip_y + 32, value, font(SANS_B, 34), (255, 255, 255))
        if i:
            draw.line([36 + cell_w * i, strip_y + 10, 36 + cell_w * i, strip_y + 68],
                      fill=(70, 92, 140), width=2)
    grid_y = strip_y + 78 + 14

    # ---- secondary stories ----------------------------------------
    stories = [
        ("CHINA", RED,
         "Chen Jining investigated",
         "Shanghai's party chief is the fourth Politburo member "
         "probed since 2025, Xinhua reports."),
        ("TRADE SECRETS", NAVY,
         "Huawei convicted in US",
         "A Brooklyn jury found the tech giant guilty on 10 of 12 "
         "counts, incl. trade-secret theft."),
        ("STRAIT OF HORMUZ", GOLD,
         "Tankers hit mines in Hormuz",
         "Iran's navy says the strait stays shut until its seven "
         "conditions are met; oil near $91."),
        ("MICROSOFT", NAVY,
         "Microsoft: 'Code Red' overhaul",
         "After the 24-hour global outage hit Outlook and Teams, "
         "the firm vows one-hour recovery."),
        ("COLOMBIA", RED,
         "25 hostage at Colombia store",
         "Gunmen seized shoppers and staff at a supermarket as "
         "police surrounded the building."),
        ("VIETNAM", GOLD,
         "Hanoi eatery blast kills 6",
         "A hot-pot restaurant explosion in the capital injured "
         "more than a dozen people."),
    ]
    col_w = (W - 72 - 16) / 2
    row_h = 100
    for idx, (tag, colour, head, body) in enumerate(stories):
        col = idx % 2
        row = idx // 2
        x0 = 36 + col * (col_w + 16)
        y0 = grid_y + row * (row_h + 10)
        draw.rectangle([x0, y0, x0 + col_w, y0 + row_h], fill=PANEL, outline=PANEL_LINE, width=2)
        draw.rectangle([x0, y0, x0 + 7, y0 + row_h], fill=colour)
        draw.text((x0 + 20, y0 + 7), tag, font=font(SANS_B, 16), fill=colour)
        draw.text((x0 + 20, y0 + 28), head, font=font(SERIF_B, 23), fill=INK)
        left_text(draw, x0 + 20, y0 + 58, body, font(SANS, 17), (62, 60, 54), col_w - 36, 21)

    # ---- footer ticker --------------------------------------------
    foot_y = grid_y + 3 * row_h + 2 * 10 + 16
    draw.rectangle([0, foot_y, W, H], fill=INK)
    ticker = [
        "US consumer confidence jumps to 103.3, a near two-year high; Shein pays $100M to the FTC.",
        "Putin vows retaliation as Ukraine keeps striking Russian oil refineries.",
        "Ahead today: US inflation and GDP data; traders price a December Fed rate hike.",
    ]
    ty = foot_y + 10
    draw.text((36, ty), "ALSO TODAY", font=font(SANS_B, 18), fill=(240, 200, 90))
    ty += 26
    for item in ticker:
        draw.text((36, ty), "-  " + item, font=font(SANS, 20), fill=(238, 236, 228))
        ty += 25

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
