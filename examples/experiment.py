from dbeval import EvalTool

e = EvalTool.EvalTool("sample_experiment")

e.clear()

db_sizes = ["1M", "5M", "10M", "50M", "100M"]
threads  = [2, 4, 8, 16, 32, 56, 64, 112]
engines  = ["vdms", "slowdb", "slowerdb"]
queries  = ["q1_desc", "q2_desc", "q3_desc", "q4_desc", "q5_desc"]

for th in threads:
    eng_offset = 1
    for eng in engines:
        eng_offset *=10
        db_size_offset = 1
        for dbs in db_sizes:
            query_offset = 0
            db_size_offset *= 2
            for q in queries:
                query_offset += 1
                e.add_row(q,
                     eng,
                     dbs,
                     th,
                     10,
                     0.0023 * query_offset * eng_offset / db_size_offset,
                     0.0023 * query_offset * eng_offset / db_size_offset * 0.4,
                     40 * db_size_offset,
                     4,
                     )

e.export_to_csv()
