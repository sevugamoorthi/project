# Cover Drive Analysis (Real-Time)

This tool processes a cricket batting video (cover drive), extracts pose per frame, computes live metrics (elbow angle, spine lean, head-over-knee, front foot angle), draws overlays, and saves:
- `/output/annotated_video.mp4` (or `.avi` fallback) – full-length with live overlays
- `/output/evaluation.json` – final multi-category scores and feedback

## 1) Setup

**Option A: pip (recommended)**
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

**Option B: conda (alternative)**
```bash
conda create -n coverdrive python=3.10 -y
conda activate coverdrive
pip install -r requirements.txt
```

> If you face OpenCV video codec issues, install `ffmpeg` on your system and retry.

## 2) Run

```bash
python cover_drive_analysis_realtime.py path/to/your_video.mp4
```
Outputs will appear in `./output/`:
- `annotated_video.mp4` (or `annotated_video.avi` if mp4 codec unavailable)
- `evaluation.json`

### Optional arguments (edit inside the script)
- `FRONT_SIDE`: `"left"` or `"right"` (which leg is front)
- `RESIZE_WIDTH`: e.g., `960` for faster processing
- Metric target ranges (edit constants at the top)

## 3) What it measures

- **Elbow angle (shoulder–elbow–wrist)** – target 100–130°
- **Spine lean vs vertical** – target 5–20°
- **Head-over-knee alignment** – normalized distance ≤ 0.20 (smaller is better)
- **Front foot angle vs x-axis** – target 15–35°

## 4) Final scoring (1–10 per category)

- **Footwork** – % of frames with front foot angle in range
- **Head Position** – median head-over-knee (lower is better)
- **Swing Control** – % elbow-in-range (proxy)
- **Balance** – % spine-lean-in-range (proxy)
- **Follow-through** – simple mix of elbow/spine/foot consistency

A short, actionable feedback list is written to `evaluation.json`.

## 5) Assumptions & Limitations

- Best with **side-on** videos where the batter is clearly visible.
- Works for one batter; crowded backgrounds/occlusions can reduce accuracy.
- Lighting, resolution, and subject size strongly affect pose quality.
- No bat tracking in the base scope.
- If FPS is low, try reducing `RESIZE_WIDTH` or using a smaller input video.

## 6) Troubleshooting

- **Cannot write mp4**: The script falls back to `.avi`. Install system `ffmpeg` if needed.
- **Pose missing often**: Improve lighting, move camera closer, ensure full body in frame.
- **Slow processing**: Lower resolution (`RESIZE_WIDTH`), or process every 2nd frame (customize loop).
