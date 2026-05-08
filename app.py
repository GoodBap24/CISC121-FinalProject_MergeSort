import gradio as gr
import time

# --- STEP 1: PREPARING THE DATA ---
def parse_input(text):
    students = []
    lines = text.strip().split('\n')
    for line in lines:
        if "," in line:
            try:
                name_part, score_str = line.split(",")
                name = name_part.strip()
                score = float(score_str.strip())
                
                # VALIDATION: Only English letters in names and scores 0-100
                if name.replace(" ", "").isalpha() and 0 <= score <= 100:
                    students.append({"name": name, "score": score, "comp": False})
            except ValueError:
                continue
    return students

# --- STEP 2: THE SORTING SIMULATION ---
def merge_sort_sim(arr):
    if len(arr) <= 1:
        yield arr
        return arr

    mid = len(arr) // 2
    
    # We must capture the final sorted list from the generator
    left_gen = merge_sort_sim(arr[:mid])
    left = None
    for step in left_gen:
        left = step
        yield left + arr[mid:]

    right_gen = merge_sort_sim(arr[mid:])
    right = None
    for step in right_gen:
        right = step
        yield left + right

    # --- THE MERGE STEP ---
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Set comparison tags
        left[i]["comp"] = True
        right[j]["comp"] = True
        yield sorted_list + left[i:] + right[j:]
        time.sleep(0.6)

        if left[i]["score"] >= right[j]["score"]:
            left[i]["comp"] = False
            sorted_list.append(left[i])
            i += 1
        else:
            right[j]["comp"] = False
            sorted_list.append(right[j])
            j += 1
        yield sorted_list + left[i:] + right[j:]

    # Clean up any remaining tags
    for s in left[i:]: s["comp"] = False
    for s in right[j:]: s["comp"] = False
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    yield sorted_list
    return sorted_list

# --- STEP 3: THE INTERFACE ---
def start_sorting(input_text):
    data = parse_input(input_text)
    if not data:
        yield "Error: Please enter valid names (letters only) and scores (0-100)."
        return

    for step in merge_sort_sim(data):
        output = ""
        for rank, s in enumerate(step, 1):
            tag = " 🟡 [COMPARING]" if s.get("comp") else ""
            output += f"{rank}. {s['name']} — {s['score']}{tag}\n"
        yield output

with gr.Blocks() as demo:
    gr.Markdown("# 🏆 Scholarship Merit Ranker")
    with gr.Row():
        input_box = gr.Textbox(label="Input (Name, Score)", value="Alice, 85\nBob, 92\nCharlie, 78\nRaelyn, 96", lines=8)
        output_box = gr.Textbox(label="Step-by-Step Sorting...", lines=12)
    btn = gr.Button("Start Simulation")
    btn.click(fn=start_sorting, inputs=input_box, outputs=output_box)

if __name__ == "__main__":
    demo.launch()
