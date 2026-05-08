import gradio as gr
import time

# --- STEP 1: PREPARING THE DATA ---
def parse_input(text):
    """Turns your text into a list, ignoring invalid scores and non-alpha names."""
    students = []
    lines = text.strip().split('\n')
    for line in lines:
        if "," in line:
            try:
                name_part, score_str = line.split(",")
                name = name_part.strip()
                score = float(score_str.strip())
                
                # NEW: Check if name is letters-only AND score is 0-100
                # (Note: name.replace(" ", "") allows for names with spaces like 'Tay Moore')
                if name.replace(" ", "").isalpha() and 0 <= score <= 100:
                    students.append({"name": name, "score": score})
            except ValueError:
                continue
    return students

# --- STEP 2: THE MERGE SORT (FLOWCHART LOGIC) ---
def merge_sort_sim(arr):
    """
    This is the Merge Sort from your flowchart.
    Instead of 'return', we use 'yield' to show the steps in the UI.
    """
    if len(arr) <= 1:
        yield arr
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # We recursively sort both halves
    # (Simplified for the simulation view)
    yield from merge_sort_sim(left)
    yield from merge_sort_sim(right)

    # --- THE MERGE STEP (Where the yellow highlights happen) ---
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        # This is the 'Comparison Diamond' from your flowchart
        # We sort DESCENDING (Higher score first)
        if left[i]["score"] >= right[j]["score"]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
        
        # We 'yield' here so the Gradio app updates the screen at every comparison
        yield sorted_list + left[i:] + right[j:]
        time.sleep(0.5) # Slows it down so you can actually see it!

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    yield sorted_list

# --- STEP 3: THE GRADIO INTERFACE (THE WEBSITE) ---
def start_sorting(input_text):
    """Function that connects the button to the algorithm."""
    data = parse_input(input_text)
    # This loop goes through every 'yield' step in our algorithm
    for step in merge_sort_sim(data):
        # We format the list nicely for the screen
        output = ""
        for rank, s in enumerate(step, 1):
            output += f"{rank}. {s['name']} — {s['score']}\n"
        yield output

# Setting up the visual boxes
with gr.Blocks() as demo:
    gr.Markdown("# 🏆 Scholarship Merit Ranker")
    gr.Markdown("Type names and scores below to see the Merge Sort algorithm in action.")
    
    with gr.Row():
        input_box = gr.Textbox(label="Input (Name, Score)", value="Alice, 85\nBob, 92\nCharlie, 78", lines=5)
        output_box = gr.Textbox(label="Step-by-Step Sorting...", lines=10)
    
    btn = gr.Button("Start Simulation")
    btn.click(fn=start_sorting, inputs=input_box, outputs=output_box)

if __name__ == "__main__":
    demo.launch() 
