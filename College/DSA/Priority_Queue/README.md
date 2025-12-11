```mermaid
flowchart TD

%% MAIN OPERATION SELECTION
A[Start] --> B{Choose Operation}

B -->|Enqueue| ENQ1
B -->|Dequeue| DEQ1
B -->|Peek| PEK1
B -->|Display| DSP1
B -->|Exit| X[End]


%% ENQUEUE OPERATION
subgraph ENQUEUE_OPERATION [Enqueue Operation]
ENQ1[Input value and priority] --> ENQ2[Create new_node(data, priority)]
ENQ2 --> ENQ3{Queue empty<br/>OR priority > front.priority?}

ENQ3 -->|Yes| ENQ4[Insert new_node at front]
ENQ4 --> ENQ_END[Return to Main]

ENQ3 -->|No| ENQ5[Set temp = front]
ENQ5 --> ENQ6{temp.next exists<br/>AND temp.next.priority ≥ priority?}

ENQ6 -->|Yes| ENQ7[Move temp = temp.next]
ENQ7 --> ENQ6

ENQ6 -->|No| ENQ8[Insert new_node after temp]
ENQ8 --> ENQ_END
end


%% DEQUEUE OPERATION
subgraph DEQUEUE_OPERATION [Dequeue Operation]
DEQ1{Queue empty?} -->|Yes| DEQ2[Print "Queue is empty"]
DEQ2 --> DEQ_END[Return to Main]

DEQ1 -->|No| DEQ3[Store front.data]
DEQ3 --> DEQ4[Move front = front.next]
DEQ4 --> DEQ_END
end


%% PEEK OPERATION
subgraph PEEK_OPERATION [Peek Operation]
PEK1{Queue empty?} -->|Yes| PEK2[Print "Queue is empty"]
PEK2 --> PEK_END[Return to Main]

PEK1 -->|No| PEK3[Print/Return front.data]
PEK3 --> PEK_END
end


%% DISPLAY OPERATION
subgraph DISPLAY_OPERATION [Display Operation]
DSP1{Queue empty?} -->|Yes| DSP2[Print "Queue is empty"]
DSP2 --> DSP_END[Return to Main]

DSP1 -->|No| DSP3[Set temp = front]
DSP3 --> DSP4{temp != None?}

DSP4 -->|Yes| DSP5[Print temp.data]
DSP5 --> DSP6[Move temp = temp.next]
DSP6 --> DSP4

DSP4 -->|No| DSP_END
end
```
