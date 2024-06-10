def needleman_wunsch(seq1, seq2, match_score, mismatch_score, gap_penalty):
    m, n = len(seq1), len(seq2)
    # Initialize the score matrix
    score = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(1, m + 1):
        score[i][0] = i * gap_penalty
    for j in range(1, n + 1):
        score[0][j] = j * gap_penalty

    # Fill the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diag_score = score[i - 1][j - 1] + match_score
            else:
                diag_score = score[i - 1][j - 1] + mismatch_score

            score[i][j] = max(score[i - 1][j] + gap_penalty,  # Up
                              score[i][j - 1] + gap_penalty,  # Left
                              diag_score)  # Diagonal

    # Trace back to find the optimal alignment
    align1, align2 = "", ""
    i, j = m, n
    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diag = score[i - 1][j - 1]
        score_up = score[i - 1][j]
        score_left = score[i][j - 1]

        if seq1[i - 1] == seq2[j - 1]:
            match = match_score
        else:
            match = mismatch_score

        if score_current == score_diag + match:
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap_penalty:
            align1 += seq1[i - 1]
            align2 += "-"
            i -= 1
        else:
            align1 += "-"
            align2 += seq2[j - 1]
            j -= 1

    # Finish tracing up to the top of the matrix
    while i > 0:
        align1 += seq1[i - 1]
        align2 += "-"
        i -= 1
    while j > 0:
        align1 += "-"
        align2 += seq2[j - 1]
        j -= 1

    # The sequences need to be reversed as we've aligned them from the end to the start
    return align1[::-1], align2[::-1], score[m][n]

# Parameters
match_score = 1
mismatch_score = -1
gap_penalty = -2

# Sequences
seq1 = "ATCG"
seq2 = "TCG"

# Perform alignment
print(needleman_wunsch(seq1, seq2, match_score, mismatch_score, gap_penalty))
