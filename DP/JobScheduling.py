"""
Given n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

Return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that enter at time X, you will be able to start another job that starts at time X.

"""
import bisect


# Top-Down Approach [Time: 0(NlogN); Space: O(N)]
def JobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    def maximumProfit(idx):                                             # Helper recursive method
        if idx == n:                                                    # Check if index equals length of the array
            return 0                                                    # Return 0
        if dp[idx] == -1:                                               # Check if value not in DP
            nextIdx = bisect.bisect_left(startTime, jobs[idx][1])       # Get the next index using binary search (log N)

            dp[idx] = max(jobs[idx][-1] + maximumProfit(nextIdx),       # Selecting the current job
                          maximumProfit(idx + 1))                       # Skipping the current job

        return dp[idx]                                                  # Return the maximum profit

    n = len(profit)                                                     # Store length of the array
    dp = [-1] * n                                                       # Initialise the DP

    jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]    # Create an array of data tuples
    jobs.sort(key=lambda x: x[0])                                       # Sort the array (for the purpose of BS)

    startTime = [job[0] for job in jobs]                                # Update the startTime array to have sorted vals

    return maximumProfit(0)                                             # Return the result


# print(JobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
# print(JobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
# print(JobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))
