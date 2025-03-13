import tkinter as tk
from tkinter import messagebox

class PageReplacementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement")
        self.root.geometry("800x600")
        

        # Variables to store user input
        self.frames_var = tk.StringVar()
        self.reference_var = tk.StringVar()
        self.algorithm_var = tk.StringVar()

        # Font settings
        self.default_font = ("Arial", 14)

        # GUI Elements
        frame = tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Number of Frames:", font=self.default_font).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.frames_entry = tk.Entry(frame, textvariable=self.frames_var, font=self.default_font)
        self.frames_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Reference String (comma-separated):", font=self.default_font).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.reference_entry = tk.Entry(frame, textvariable=self.reference_var, font=self.default_font)
        self.reference_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Page Replacement Algorithm:", font=self.default_font).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.algorithm_menu = tk.OptionMenu(frame, self.algorithm_var, "FIFO", "LRU", "Optimal", "MRU")
        self.algorithm_menu.config(font=self.default_font)
        self.algorithm_menu.grid(row=2, column=1, padx=5, pady=5)

        self.run_button = tk.Button(frame, text="Run", command=self.run_algorithm, font=self.default_font, bg="skyblue", fg="black")
        self.run_button.grid(row=3, columnspan=2, padx=5, pady=10, sticky="ew")

        # Buttons to show algorithm information
        self.fifo_info_button = tk.Button(frame, text="FIFO Info", command=self.show_fifo_info, font=self.default_font, bg="lightgreen", fg="black")
        self.fifo_info_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        self.lru_info_button = tk.Button(frame, text="LRU Info", command=self.show_lru_info, font=self.default_font, bg="lightcoral", fg="black")
        self.lru_info_button.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        self.optimal_info_button = tk.Button(frame, text="Optimal Info", command=self.show_optimal_info, font=self.default_font, bg="lightyellow", fg="black")
        self.optimal_info_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        self.mru_info_button = tk.Button(frame, text="MRU Info", command=self.show_mru_info, font=self.default_font, bg="lightpink", fg="black")
        self.mru_info_button.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

    def run_algorithm(self):
        frames = self.frames_var.get()
        reference_str = self.reference_var.get()
        algorithm = self.algorithm_var.get()

        try:
            frames = int(frames)
            reference_list = list(map(int, reference_str.split(',')))

            if algorithm == "FIFO":
                self.run_fifo(frames, reference_list)
            elif algorithm == "LRU":
                self.run_lru(frames, reference_list)
            elif algorithm == "Optimal":
                self.run_optimal(frames, reference_list)
            elif algorithm == "MRU":
                self.run_mru(frames, reference_list)
            else:
                messagebox.showerror("Error", "Invalid algorithm selection.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter integers.")

    def run_fifo(self, frames, reference_list):
        frame_queue = []
        page_faults = 0
        hits = 0
        frame_states = []

        for page in reference_list:
            if page in frame_queue:
                hits += 1
            else:
                if len(frame_queue) == frames:
                    frame_queue.pop(0)
                frame_queue.append(page)
                page_faults += 1
            
            frame_states.append(list(frame_queue))

        total_pages = len(reference_list)
        hit_ratio = hits / total_pages
        fault_ratio = page_faults / total_pages

        self.show_custom_info("FIFO Result", f"Page Faults: {page_faults}\nHits: {hits}\nHit Ratio: {hit_ratio:.2f}\nFault Ratio: {fault_ratio:.2f}\nFrames:\n{frame_states}", 26)

    def run_lru(self, frames, reference_list):
        frame_queue = []
        page_faults = 0
        hits = 0
        frame_states = []

        for page in reference_list:
            if page in frame_queue:
                frame_queue.remove(page)
                frame_queue.append(page)
                hits += 1
            else:
                if len(frame_queue) == frames:
                    frame_queue.pop(0)
                frame_queue.append(page)
                page_faults += 1
            
            frame_states.append(list(frame_queue))

        total_pages = len(reference_list)
        hit_ratio = hits / total_pages
        fault_ratio = page_faults / total_pages

        self.show_custom_info("LRU Result", f"Page Faults: {page_faults}\nHits: {hits}\nHit Ratio: {hit_ratio:.2f}\nFault Ratio: {fault_ratio:.2f}\nFrames:\n{frame_states}", 16)

    def run_optimal(self, frames, reference_list):
        frame_queue = []
        page_faults = 0
        hits = 0
        frame_states = []

        for page in reference_list:
            if page in frame_queue:
                hits += 1
            else:
                if len(frame_queue) == frames:
                    furthest_used_index = -1
                    for frame_page in frame_queue:
                        if frame_page not in reference_list[reference_list.index(page)+1:]:
                            furthest_used_index = frame_queue.index(frame_page)
                            break
                    if furthest_used_index == -1:
                        furthest_used_index = frame_queue.index(reference_list[-1])
                    frame_queue[furthest_used_index] = page
                else:
                    frame_queue.append(page)
                page_faults += 1
            
            frame_states.append(list(frame_queue))

        total_pages = len(reference_list)
        hit_ratio = hits / total_pages
        fault_ratio = page_faults / total_pages

        self.show_custom_info("Optimal Result", f"Page Faults: {page_faults}\nHits: {hits}\nHit Ratio: {hit_ratio:.2f}\nFault Ratio: {fault_ratio:.2f}\nFrames:\n{frame_states}", 26)

    def run_mru(self, frames, reference_list):
        frame_queue = []
        page_faults = 0
        hits = 0
        frame_states = []

        for page in reference_list:
            if page in frame_queue:
                frame_queue.remove(page)
                hits += 1
            else:
                if len(frame_queue) == frames:
                    frame_queue.pop(-1)
                page_faults += 1
            frame_queue.insert(0, page)
            frame_states.append(list(frame_queue))

        total_pages = len(reference_list)
        hit_ratio = hits / total_pages
        fault_ratio = page_faults / total_pages
        
        self.show_custom_info("MRU Result", f"Page Faults: {page_faults}\nHits: {hits}\nHit Ratio: {hit_ratio:.2f}\nFault Ratio: {fault_ratio:.2f}\nFrames:\n{frame_states}", 26)

    def show_fifo_info(self):
        self.show_custom_info("Theory of Different Algorithms", 
                              "\n The simplest page-replacement algorithm is a first-in, first-out (FIFO) algorithm.A FIFO replacement algorithm associates "
                              "\n with each page the time when that page was brought into memory.When a page must be replaced, the oldest page is chosen"                  
                             "\n Whe a page must be replaced, the oldest page is chosen. We can create a FIFO queue to hold all pages in memory.We replace"
                              "\n page at the head of the queue. When a page is brought into memory, we insert it at the tail of the queue .On the one hand,"
                            " \n \n the page replaced maybe an initialization module that was used a long time ago and is no longer needed.On the other hand,"
                            "\n it could contain a heavily used variable that was initialized early and is in constant use.Even if we select for replacement"
                           "\npage that is in active use, everything still works correctly.After we replace an active page with a new one, fault occurs almost"
                           "\n immediately to retrieve the active page.Some other page must be replaced to bring the active page back into memory."
                           "\n \n Thus, a bad replacement choice increases the page-fault rate and slows process execution. It does not, however, cause"
                           
                            "\n incorrect execution .Its time complexity is chiefly governed by the data structure employed for maintaining the FIFO queue."
                            "\nWith a simple queue implementation, insertion and removal of pages occur in constant time, denoted as O(1). However,"
                            "\n searching for a specific page within the queue can demand linear time complexity, O(n), where n represents the number of page"
                            " \n currently resident in memory. This arises from the potential need to traverse the entire queue to locate the desired page."
                            "\n  Irrespective of the number of frames, the space complexity related to maintaining the FIFO queue remains O(n), proportional"
                            "\n to the count of page frames. ", 16)

    def show_lru_info(self):
        self.show_custom_info("Theory of Different Algorithms", 
                              "\nLRU (Least Recently Used) is a page replacement algorithm that replaces the least recently used page in the memory with new page."
                              "\n LRU maintains a record of the order in which pages are accessed. When a page is accessed, it is moved to the front of the list,"
                              "\n indicating that it is the most recently used. When a page needs to be replaced, the page at the end of the list is chosen for"
                              "\n eviction. The LRU algorithm is known for its simplicity and effectiveness in capturing temporal locality, which is the tendency"
                              "\n of programs to access the same data repeatedly over a short period of time. By evicting the least recently used pages, LRU aims "
                              "\nto minimize the number of page faults and improve overall system performance.However, LRU does have limitations, particularly in "
                              "\nterms of its implementation complexity and the overhead of maintaining the access order of pages. In systems with large memory "
                              "\nsizes or high access rates, the overhead of maintaining the LRU list can become significant. "
                              "\n \n \n The time complexity of the Least Recently Used (LRU) page replacement algorithm is O(1) per page access operation due to"
                              "\n its efficient data structures like doubly linked lists and hash tables. Its space complexity is O(n), where n is the number of "
                              "\npage frames allocated for storing pages in memory, as it requires additional storage for maintaining page access order and "
                              "\ntracking page presence. Despite the space overhead, LRU's effectiveness in minimizing page faults makes it a practical choice "
                              "\nfor memory management."

                               "\n ", 16)

    def show_optimal_info(self):
        self.show_custom_info("Theory of Different Algorithms", 
                              "\nOptimal Page Replacement is a theoretical algorithm that selects the page for replacement which will not be used for the longest"
                              " \ntime in the future.The OPTIMAL Page Replacement Algorithms works on a certain principle. The principle is:Replace the Page which "
                              "\nis not used in the Longest Dimension of time in future.This principle means that after all the frames are filled then, see the"
                              "\n future pages which are to occupy the frames. Go on checking for the pages which are already available in the frames. Choose "
                              "\nthe page which is at last.The Optimal page replacement algorithm minimizes page faults by selecting the page that won't be used "
                              "\nfor the longest time. Its advantages lie in theoretical optimality, useful for benchmarking. However, it's impractical due to the"
                              "\n need for future knowledge of page accesses and high computational complexity, making it unsuitable for real-world systems."
                              "\n \n \n The space complexity of the Optimal page replacement algorithm is relatively low. It primarily involves storing information about "
                              "\nthe pages currently in memory and their future references. Typically, this information can be represented using data structures "
                              "\nlike arrays or linked lists. Therefore, the space complexity is O(n), where n is the number of page frames allocated for storing pages"
                              "\nRegarding time complexity, determining the optimal page to replace involves analyzing future page references. In the worst-case "
                              "\nscenario, this would require scanning through all future references to identify the page that won't be used for the longest time. "
                              "\nThus, the time complexity for each page replacement operation can be considered O(m), where m is the number of pages remaining "
                              "\nin the memory at the time of replacement."
                              "\n", 16)

    def show_mru_info(self):
        self.show_custom_info("MRU Algorithm", 
                              "\nMost Recently Used (MRU) is a page replacement algorithm that replaces the most recently used page in the memory with "
                              "\n the new page.this means that the page that was accessed most recently is considered the most valuable and is kept "
                              "\nin memory.In terms of efficiency, the MRU algorithm operates similarly to the LRU algorithm but in reverse.When a page"
                              "\n  is accessed, it is moved to the front of the access list. Then, when a page needs to be replaced, the page at the front "
                              "\n of the list (the most recently used) is chosen for eviction.The MRU algorithm is relatively simple to implement and can be"
                              "\n  effective in scenarios where programs exhibit patterns of accessing  the same data repeatedly in a short period. However, "
                              "\n it may  not perform optimally in situations where there is frequent alternation  between different sets of data, as it many"
                              "\n mistakenly evict pages that are actually still in active use."
                       "\n \n \n The time complexity of the Most Recently Used (MRU) page replacement algorithm is O(1) per page access operation, as it  "
                              "\n  efficiently maintains a data structure to track the order of page accesses, enabling quick identification of the "
                              "\n  most recently used page.In terms of space complexity, MRU requires additional storage for this data structure, typicallys"
                              "\n   a list or array, which depends on the number of page frames allocated for storing page memory. Hence, its space complexity "
                              "\n is O(n), where n represents the number of page frames. Despite this overhead, MRU's effectiveness in minimizing page faults . "
                              "\n makes it suitable for certain memory management scenarios", 16)
  
    def show_custom_info(self, title, message, font_size):
       top = tk.Toplevel(self.root)
       top.title(title)
       label = tk.Label(top, text=message, font=("Arial", font_size))
       label.pack(padx=20, pady=10)
       button = tk.Button(top, text="OK", command=top.destroy)
       button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    
    app = PageReplacementApp(root)
  
    root.mainloop()

