# huytruongthuyng2.github.io
- Which paper you chose

R. Krishna, K. Hata, S. Chen, J. Kravitz, D.A. Shamma, L. Fei-Fei, M.S. Bernstein. "Embracing error to enable rapid crowdsourcing." CHI 2016.

- A list of the people you discussed this assignment with, or else an explicit statement that you had no collaborators. This is an individual assignment, so be aware of the course's collaboration policy. 

I had no collaborators.

- The URL of your YouTube/Vimeo screencast

- The URL of your experiment implementation

https://huytruongthuyng2.github.io/

- How are tasks sequenced in your experimental implementation
  - The first task is the control condition where image transition is self-paced and the user is asked to press Y on their keyboard if they see a dog and N otherwise. The detailed instructions are displayed at the beginning of this task. 
  - After the first task is completed, the second task is displayed. The second task is the experimental condition where image transition happens every 500ms (it is 100ms in the research paper but the Professor said it would be better to have it 500ms). The detailed instructions are also displayed at the beginning of this task. 
  - After the second task if completed, the page will let the user know that the experiment is done and they can exit.
  
- What are the experimental parameters in your implementation? How can they be adjusted?

The experimental parameters include: 

  - The number of images used in the control condition (specified in the constant variable named numImagesInPartOne)
  - The number of images used in the experimental condition (specified in the constant variable named numImagesInPartTwo)
  - The transition time of images in the experimental condition (specified in the constant variable named imageTransitionSpeed)
  
These parameters can be adjusted by simply changing these assigned numbers of the variables in the source code: index.html > html tag > head tag > script tag.

- What data is collected for each trial run and in what format?

In each trial run, the following data are collected:
  - In the control condition, I am collecting each image name, if the image shows dog, user's reaction time, and the user's choice. Therefore, if there are 10 images in this condition, 10 rows of data will be collected with each row has the following format: user_unique_id, image_name, image_positive?, reaction_time, worker_choice, N/A, N/A, N/A.
  - In the experimental condition, I am collecting each image name, if the image shows dog, if the user clicked. Therefore, if there are 100 images in this condition, 100 rows of data will be collected with each row has the following format: user_unique_id, N/A, N/A, N/A, N/A, image_name, image_positive?, worker_clicked?.
  - IMPORTANT NOTE: N/A values are used to fill up the row of data so they all have the same length for the convenience of Google Form logging.
- What demographic data or subjective judgements do you collect from each user, and why?

In the research paper, no demographic data or subjective judgements are being collected so I am not collecting any in this interface implementation.

