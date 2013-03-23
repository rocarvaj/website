#Scheduling jobs with the "at" command

- date: 2013-02-13
- tags: tips
- category: work

-----

Picture the following scenario. It's midnight and you have to run a large number of jobs
in a cluster using, let's say, Condor. You don't want to submit all of your jobs at once,
because it might have a negative effect in your priority in the queue, but you also don't want
spend the whole night sending jobs in batches.

A solution is to use the Unix [`at`](http://unixhelp.ed.ac.uk/CGI/man-cgi?at) command. I'll
just show an example, assume that you have a script `runner.sh` that 
