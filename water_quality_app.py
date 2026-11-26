from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AquaCheck — Water Quality Snapshot</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--ink:#122a35;--muted:#66808c;--sea:#147e91;--mint:#dff4ef;--bg:#f3f8f8;--line:#dce9eb}*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 85% 0%,#e1f4f2 0,transparent 40%),var(--bg);font-family:"DM Sans",sans-serif;color:var(--ink)}.shell{max-width:1120px;margin:auto;padding:36px 22px 70px}header{display:flex;align-items:center;justify-content:space-between;margin-bottom:34px}.brand{display:flex;align-items:center;gap:12px;font-family:Manrope,sans-serif;font-weight:800;font-size:21px;letter-spacing:-.4px}.logo{width:42px;height:42px;border-radius:14px;background:#0f7185;color:#fff;display:grid;place-items:center;box-shadow:0 8px 18px #147e9130}.logo svg{width:23px}.tag{border:1px solid #cce4e3;border-radius:999px;padding:9px 13px;color:#4d7782;font-size:12px;font-weight:700;letter-spacing:.5px}.hero{margin-bottom:28px}.eyebrow{color:#167c8e;font-weight:800;letter-spacing:1.5px;font-size:11px;text-transform:uppercase;margin-bottom:12px}h1{font-family:Manrope,sans-serif;font-size:clamp(30px,5vw,46px);line-height:1.1;letter-spacing:-1.6px;margin:0 0 12px}.hero p{color:var(--muted);font-size:15px;line-height:1.65;max-width:680px;margin:0}.layout{display:grid;grid-template-columns:1.12fr .88fr;gap:20px;align-items:stretch}.panel{background:#fff;border:1px solid var(--line);border-radius:24px;padding:24px;box-shadow:0 14px 35px #12313e08}.panel-heading{display:flex;justify-content:space-between;align-items:center;margin-bottom:21px}.panel-heading h2{font-family:Manrope,sans-serif;font-size:18px;margin:0;letter-spacing:-.4px}.small-label{font-size:11px;color:#7b929c;font-weight:700}.inputs{display:flex;flex-direction:column;gap:14px}.metric{display:grid;grid-template-columns:1fr auto;gap:12px;align-items:center;border:1px solid #e5eef0;border-radius:16px;padding:14px 15px;background:#fbfdfd}.metric label{font-size:13px;font-weight:700;display:block;margin-bottom:6px}.metric input,.metric select{width:100%;max-width:220px;border:0;background:transparent;outline:none;font-family:Manrope,sans-serif;font-size:21px;font-weight:800;color:#163744}.metric input::placeholder{color:#c0d0d5}.unit{font-size:12px;font-weight:700;color:#71909b}.standard{font-size:11px;color:#78909b;margin-top:4px}.ph-select{appearance:auto;cursor:pointer}.ph-colorbar{height:8px;max-width:220px;border-radius:10px;margin-top:7px;background:linear-gradient(90deg,#d64c54,#ee9d46,#f0db62,#8ed37c,#48b5a4,#6a83d2,#9a63bd)}
.ph-picker{display:grid;grid-template-columns:repeat(14,minmax(0,1fr));gap:5px;margin:7px 0 8px}
.ph-choice{width:100%;min-width:0;margin:0;padding:10px 0;border:2px solid transparent;border-radius:7px;background:var(--ph-color);color:#fff;font:700 12px "DM Sans";box-shadow:none;transition:transform .15s,border-color .15s;line-height:1}
.ph-choice:hover{transform:translateY(-2px);filter:brightness(1.05)}
.ph-choice.selected{border-color:#173e4a;box-shadow:0 0 0 2px #fff inset}
@media(max-width:560px){.ph-picker{grid-template-columns:repeat(7,minmax(0,1fr))}.ph-choice{padding:12px 0}}
button{width:100%;margin-top:17px;border:0;border-radius:14px;padding:14px;background:linear-gradient(110deg,#147e91,#1b9a9c);color:white;font:700 14px "DM Sans";cursor:pointer;box-shadow:0 10px 18px #178a9728;transition:.2s}button:hover{transform:translateY(-1px);filter:brightness(1.04)}.result{background:linear-gradient(150deg,#0d3948,#12576a);color:white;position:relative;overflow:hidden;min-height:410px}.result:after{content:"";position:absolute;width:240px;height:240px;border:1px solid #ffffff12;border-radius:50%;right:-75px;top:-75px;box-shadow:0 0 0 28px #ffffff06,0 0 0 58px #ffffff04}.result .panel-heading h2{color:white}.result .small-label{color:#b9d4dc}.status-pill{display:inline-flex;align-items:center;gap:8px;background:#ffffff12;border:1px solid #ffffff20;border-radius:100px;padding:7px 11px;color:#d7eff2;font-size:11px;font-weight:700}.status-dot{width:7px;height:7px;border-radius:50%;background:#7de2c0}.score-wrap{margin:23px 0 18px;position:relative;z-index:1}.score{font-family:Manrope,sans-serif;font-size:60px;font-weight:800;letter-spacing:-3px;line-height:1}.score span{font-size:17px;letter-spacing:0;color:#a8d3dc;font-weight:600}.scale{height:9px;border-radius:20px;background:linear-gradient(90deg,#ee8e76 0%,#f2c86d 38%,#80d2b3 68%,#4fb7c3 100%);margin:16px 0 9px;position:relative}.marker{position:absolute;top:-4px;width:17px;height:17px;background:white;border:4px solid #164b5c;border-radius:50%;left:0;transition:left .35s}.scale-labels{display:flex;justify-content:space-between;font-size:10px;color:#b4d2dc}.result-title{font-family:Manrope,sans-serif;font-size:21px;font-weight:800;margin:18px 0 7px;position:relative;z-index:1}.result-copy{font-size:13px;line-height:1.6;color:#c2dce3;max-width:370px;position:relative;z-index:1}.advisory{font-size:11px;color:#c6dce0;border-top:1px solid #ffffff1c;padding-top:15px;margin-top:20px;line-height:1.55}.solutions{margin-top:22px}.solutions .panel-heading{margin-bottom:12px}.solution-list{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.solution-card{background:#fbfdfd;border:1px solid var(--line);border-radius:16px;padding:16px}.solution-card h3{font-size:13px;margin:0 0 8px;font-weight:800}.solution-card p{font-size:12px;line-height:1.6;color:#6c8791;margin:0}.no-results{font-size:13px;color:#718994;padding:14px;background:#f6fafb;border-radius:13px}.notice{font-size:12px;color:#9a6553;padding:12px;border-radius:12px;background:#fff4ec;margin-top:12px}footer{text-align:center;font-size:11px;color:#89a0a8;margin-top:25px}@media(max-width:780px){.layout{grid-template-columns:1fr}.result{min-height:360px}.solution-list{grid-template-columns:1fr}.shell{padding:24px 16px 50px}header{margin-bottom:28px}}
</style></head><body><div class="shell"><header><div class="brand"><div class="logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s-7 8-7 12a7 7 0 0 0 14 0c0-4-7-12-7-12z"/><path d="M8.5 16a3.5 3.5 0 0 0 3.5 3"/></svg></div>AquaCheck</div><div class="tag">WATER QUALITY SNAPSHOT</div></header>
<section class="hero"><div class="eyebrow">Know what's in your water</div><h1>A clearer picture.<br>One drop at a time.</h1><p>Enter any reading you have to get a quick screening snapshot and practical next steps. Leave other fields blank if you haven't measured them yet.</p></section>
<div class="layout"><section class="panel"><div class="panel-heading"><h2>Your water readings</h2><span class="small-label">Any 1 or more</span></div><form id="readings-form" method="POST"><div class="inputs">
<div class="metric"><div><label for="ph">Universal coded pH (test strip)</label><input type="hidden" id="ph" name="ph" value="{{ph or ''}}">
<div class="ph-picker" role="group" aria-label="Choose pH colour from 1 to 14">
{% for p in range(1,15) %}
<button type="button" class="ph-choice {% if ph|string == p|string %}selected{% endif %}" data-ph="{{p}}" aria-pressed="{{ 'true' if ph|string == p|string else 'false' }}" style="--ph-color: {{ph_colors[p-1]}}">{{p}}</button>
{% endfor %}
</div>
<div class="ph-colorbar" aria-label="Universal pH colour spectrum"></div><div class="standard">Universal test-strip scale: 1–14 · Typical guideline: 6.5–8.5</div></div><span class="unit">pH</span></div>
<div class="metric"><div><label for="turbidity">Turbidity</label><input id="turbidity" name="turbidity" type="number" min="0" step="any" placeholder="e.g. 0.8" value="{{turbidity or ''}}"><div class="standard">Target: ≤ 1 NTU (clear water)</div></div><span class="unit">NTU</span></div>
<div class="metric"><div><label for="tds">Total dissolved solids</label><input id="tds" name="tds" type="number" min="0" step="any" placeholder="e.g. 240" value="{{tds or ''}}"><div class="standard">Taste guideline: ≤ 500 ppm</div></div><span class="unit">ppm</span></div></div><button type="submit">Analyze entered readings →</button></form>{% if input_error %}<div class="notice">{{input_error}}</div>{% endif %}</section>
<section class="panel result"><div class="panel-heading"><h2>Quality snapshot</h2><span class="status-pill"><i class="status-dot"></i> SCREENING ONLY</span></div>
{% if score is not none %}<div class="score-wrap"><div class="score">{{score}}<span>/100</span></div><div class="scale"><div class="marker" style="left:calc({{score}}% - 8px)"></div></div><div class="scale-labels"><span>Needs attention</span><span>Better readings</span></div></div><div class="result-title">{{headline}}</div><div class="result-copy">{{summary}}</div>
{% else %}<div class="score-wrap"><div class="score">—<span>/100</span></div><div class="scale"><div class="marker" style="left:0%"></div></div><div class="scale-labels"><span>Needs attention</span><span>Better readings</span></div></div><div class="result-title">Ready when you are</div><div class="result-copy">Enter just one reading—or as many as you have—to receive a screening result.</div>{% endif %}
<div class="advisory">Important: pH, turbidity and TDS alone cannot establish that water is safe to drink. Microbial contaminants and other chemicals may be present even when these readings look good.</div></section></div>
<section class="panel solutions"><div class="panel-heading"><h2>Target the issue</h2><span class="small-label">Possible next steps</span></div>{% if advice %}<div class="solution-list">{% for item in advice %}<div class="solution-card"><h3>{{item[0]}}</h3><p>{{item[1]}}</p></div>{% endfor %}</div>{% else %}<div class="no-results">Enter at least one reading above to see issue-specific suggestions. For drinking-water safety, confirm with certified testing.</div>{% endif %}</section>
<footer>Guideline values are screening references only. Local standards and certified testing take precedence.</footer></div>
<script>
const readingsForm = document.getElementById("readings-form");

document.querySelectorAll(".ph-choice").forEach(function(choice){
  choice.addEventListener("click", function(){
    document.getElementById("ph").value = choice.dataset.ph;
    document.querySelectorAll(".ph-choice").forEach(function(item){
      const active = item === choice;
      item.classList.toggle("selected", active);
      item.setAttribute("aria-pressed", active ? "true" : "false");
    });
    readingsForm.requestSubmit();
  });
});

// Recalculate after a numeric reading is changed (when the field is committed).
["turbidity", "tds"].forEach(function(fieldId){
  const field = document.getElementById(fieldId);
  field.addEventListener("change", function(){
    readingsForm.requestSubmit();
  });
});
</script>
</body></html>'''


def analyze(ph, turbidity, tds):
    available = []
    advice = []
    issues = []
    if ph is not None:
        if ph < 6.5 or ph > 8.5:
            available.append(72)
            if ph < 6.5:
                issues.append("pH is below the typical guideline range.")
                advice.append(("Low pH (acidic)", "Test-strip reading is below the typical range. Confirm with a calibrated test and ask a water professional to assess the source; avoid adding treatment chemicals based on strip readings alone."))
            else:
                issues.append("pH is above the typical guideline range.")
                advice.append(("High pH (alkaline)", "Confirm the strip reading and seek appropriate water testing. Treatment depends on the source and cause."))
        else:
            available.append(100)
            advice.append(("pH within typical range", "The strip suggests pH is within the reference range. Strip colour matching can be approximate; this alone does not establish drinking-water safety."))
    if turbidity is not None:
        if turbidity > 1:
            available.append(max(0, 75 - min(35, turbidity * 3)))
            issues.append("Turbidity is above the clear-water target.")
            advice.append(("Elevated turbidity", "Look for sediment or source disturbance. Settling or suitable filtration may reduce particles, but validated disinfection and testing are still needed before drinking."))
        else:
            available.append(100)
            advice.append(("Low turbidity reading", "Water appears clear by this measure. Clear water can still contain microbes; turbidity is not a disinfection test."))
    if tds is not None:
        if tds > 500:
            available.append(max(0, 80 - min(35, (tds - 500) / 30)))
            issues.append("TDS is above the commonly used taste guideline.")
            advice.append(("Elevated TDS", "A TDS reading does not identify which dissolved substances are present. Get laboratory testing to identify constituents; select any treatment based on those results."))
        else:
            available.append(100)
            advice.append(("TDS within taste guideline", "TDS is within the commonly used taste/acceptability guideline. It cannot rule out specific contaminants."))
    score = round(sum(available) / len(available)) if available else None
    if score is None:
        return None, "No readings entered", "Enter at least one value to generate a screening snapshot.", []
    if issues:
        headline = "Further testing recommended"
        summary = "Based on the value(s) you entered: " + " ".join(issues) + " The score reflects only entered measurements and is not a potability verdict."
    else:
        headline = "Entered readings within targets"
        summary = "The value(s) you entered fall within the selected screening targets. Unmeasured parameters are not included; these readings cannot confirm water is safe to drink."
    return score, headline, summary, advice


@app.route('/', methods=['GET', 'POST'])
def index():
    score = headline = summary = None
    advice = []
    ph = turbidity = tds = ""
    input_error = ""
    if request.method == 'POST':
        try:
            ph_raw = request.form.get('ph', '').strip()
            turbidity_raw = request.form.get('turbidity', '').strip()
            tds_raw = request.form.get('tds', '').strip()
            if not any([ph_raw, turbidity_raw, tds_raw]):
                input_error = "Please enter at least one measurement to analyze."
            else:
                ph = int(ph_raw) if ph_raw else None
                turbidity = float(turbidity_raw) if turbidity_raw else None
                tds = float(tds_raw) if tds_raw else None
                if (ph is not None and not 1 <= ph <= 14) or (turbidity is not None and turbidity < 0) or (tds is not None and tds < 0):
                    raise ValueError
                score, headline, summary, advice = analyze(ph, turbidity, tds)
        except (TypeError, ValueError):
            score = None
            headline = "Please check your inputs"
            summary = "Choose pH from 1–14 and enter non-negative turbidity and TDS values. You may leave any field blank."
            advice = [("Check the measurements", "Use NTU for turbidity, ppm for TDS, and select the pH value that best matches the test strip colour chart.")]
    ph_colors = [
        "#d94b55", "#e96e4e", "#ed9946", "#f0c95c",
        "#d9df63", "#a9d46f", "#79c98c", "#49b6a5",
        "#42a6bd", "#6b84d3", "#8067c8", "#9b62bd",
        "#b653a9", "#913b86"
    ]
    return render_template_string(PAGE, score=score, headline=headline, summary=summary, advice=advice, ph=ph, ph_colors=ph_colors, turbidity=turbidity, tds=tds, input_error=input_error)


if __name__ == '__main__':
    app.run(debug=True)
