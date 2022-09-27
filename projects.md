---
layout: page
permalink: /projects/index.html
title: Projects
---

# Work Projects

## GoDaddy Domain Appraisals

While at GoDaddy, I created a system that uses neural networks to predict the
resale price of a domain name in the aftermarket.  GoDaddy Domain Appraisals
(GoValue) is available to millions of GoDaddy customers and provides estimated
values to help both buyers and sellers more effectively price domain names.
GoValue is 1.25x better at predicting past domain name sale prices than
human experts.  You can [try it yourself], [learn how it works], or listen
to me [talk about it on a podcast].

[try it yourself]: https://www.godaddy.com/domain-value-appraisal
[learn how it works]: https://www.godaddy.com/engineering/2019/07/26/domain-name-valuation/
[talk about it on a podcast]: https://blogs.nvidia.com/blog/2018/03/08/ai-podcast-godaddy-ai-to-domains/
[research paper]: https://arxiv.org/abs/1806.11222

## Google Native Client

While interning at Google in 2010, I added support for sandboxing
self-modifying code to Native Client (part of Google Chrome) to support
dynamic language runtimes and JIT compilers. Native Client is a sandbox
for running untrusted machine code in the web browser.  We
[published this work in PLDI](http://groups.csail.mit.edu/commit/papers/2011/ansel-pldi11-nacljit.pdf).

# Research Projects

## [OpenTuner]

[OpenTuner] is an open-source framework building domain-specific
multi-objective program autotuners.  OpenTuner supports customizable
configuration representations, an extensible technique representation
to allow for domain-specific techniques, and an easy to use interface for
communicating with the tuned program.  I was the primary author and original
creator of this project.

## [PetaBricks]
[PetaBricks] is a language and compiler where algorithmic choices are
exposed explicitly to create programs that define a search space of possible
algorithms.  The PetaBricks compiler then uses empirical autotuning to search
over these algorithms for an optimal version.  I was the primary author and
original creator of this project.


## [Kendo]
[Kendo] is a library that allows multithreaded programs,
that would normally produce non-deterministic output, to execute
deterministically by enforcing a dynamically computed and efficient
ordering of lock acquisitions.  The primary author of this work is
[Marek Olszewski](https://www.linkedin.com/in/marekolszewski/).


## [DMTCP]
[DMTCP][DMTCP] (Distributed Multi-Threaded Checkpointing) is a tool to
transparently checkpoint and restart the state of a distributed cluster
computation that communicates through MPI or sockets.  It works on unmodified
binaries at the user level.  I was the first author on the original DMTCP
paper and designed and implemented the distributed component that converted a
single-process checkpointer into a distributed checkpointer. 
I have moved on from this project, but it is continued by
many wonderful researchers, and there are now [100+ refereed
publications](http://dmtcp.sourceforge.net/publications.html) using or
extending DMTCP.


# Side Projects

## Algorithmic Trading on LendingClub.com

Since 2012 I've been doing algorithmic trading on the secondary market of
the peer-to-peer lending platform [LendingClub]. I use neural networks to
predict the likelihood of default of specific loans, and then both buy and sell
notes based on those predictions. The latest version of this is not open
source because there is a limited supply of notes available on the secondary
market. In the first few years, this was very profitable; however, recently,
other players have entered the market.  Good deals disappear within seconds,
and overall yields and volumes have fallen. To be competitive, you increasingly
need to focus on the speed of your algorithm.

[LendingClub]: https://lendingclub.com/
[GitHub Page]: https://github.com/jansel
[ShowDB]: https://github.com/jansel/showdb
[LendingClubChecker]: https://github.com/jansel/lendingclubchecker
[OpenTuner]: http://opentuner.org/
[PetaBricks]: http://projects.csail.mit.edu/petabricks/
[Kendo]: http://projects.csail.mit.edu/kendo/
[DMTCP]: http://dmtcp.sourceforge.net/


