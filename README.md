# 🏭 Multithreaded Production Line Simulator

> A concurrent manufacturing pipeline simulation written in Python using threads.  
> Four machines run in parallel, passing pieces through an inventory until a final product is assembled — or a failure halts the line.

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚙️ Parallel machines | Each machine runs as an independent thread |
| 📦 Shared inventory | Thread-safe piece exchange between machines using locks |
| 💥 Random failures | Each machine has a configurable failure probability |
| 🛑 Global halt | Any broken machine immediately stops the entire production line |
| ✅ Success detection | Machine D signals completion when the final product is made |

---

## 🔧 Production Pipeline

```
Machine A ──→ Piece1 ──┐
                        ├──→ Machine C ──→ Piece3 ──→ Machine D ──→ FinalProduct
Machine B ──→ Piece2 ──┘
```

| Machine | Processing time | Failure chance | Input | Output |
|---|---|---|---|---|
| A | 3s | 1% | *(none)* | `Piece1` |
| B | 4s | 3% | *(none)* | `Piece2` |
| C | 2s | 5% | `Piece1` + `Piece2` | `Piece3` |
| D | 2s | 2% | `Piece3` | `FinalProduct` |

---

## 🧵 Concurrency Design

| Mechanism | Purpose |
|---|---|
| `threading.Thread` | Each `Machine` runs as its own thread |
| `inventory_lock` | Prevents race conditions when reading/writing the shared inventory |
| `production_lock` | Safely broadcasts the global failure flag across all threads |
| Polling loop (`sleep 0.1s`) | Machines wait for required input pieces without busy-waiting |

---

## 📁 Project Structure

```
production-line/
└── main.py     # Machine class + pipeline setup + thread management
```

---

## 🚀 Getting Started

### Requirements

Python 3.x — no external dependencies (uses built-in `threading`, `random`, `time`)

### Run

```bash
python main.py
```

---

## 🖥️ Sample Output

```
machine A is working
machine B is working
machine A produced Piece1
machine B produced Piece2
machine C is working
machine C produced Piece3
machine D is working
machine D produced FinalProduct
The production was completed successfully
```

Or on failure:

```
machine C is broken
production failed
```

---

## ⚙️ Configuration

To customize the pipeline, edit the machine definitions in `main.py`:

```python
Machine(name, processing_time, failure_chance, input_pieces, output_piece)
```

```python
m1 = Machine("A", 3, 1,  [],                  "Piece1")
m2 = Machine("B", 4, 3,  [],                  "Piece2")
m3 = Machine("C", 2, 5,  ["Piece1","Piece2"], "Piece3")
m4 = Machine("D", 2, 2,  ["Piece3"],          "FinalProduct")
```

`failure_chance` is an integer from 1–100 representing the percentage probability of breakdown.

---

## 👩‍💻 Author

**Sepideh Pashayan**
