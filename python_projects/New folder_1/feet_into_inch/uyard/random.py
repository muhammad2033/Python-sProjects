from mimetypes import init


class MulitlevedFeedbackQueue():
    def __init__(self,queue_list,q_first):
        self.queue_list=queue_list
        self.q_first=q_first
    def scheduling(self):
        q_list=self.queue_list # Current queue set 
        q_first=self.q_first # The time slice of the first queue 
        for i in range(len(q_list)):
# Determine the time slice for each queue 
            if i==0:
                q_list[i].q=q_first
            else :
                q_list[i].q=q_list[i-1].q*2
# Time slice execution starts from the first queue 
# First judge whether it is the last queue , The last queue is executed directly RR Scheduling algorithm 
# If it's not the last queue , After executing the current queue time slice, judge whether it is necessary to join the end of the next queue 
            if i==len(q_list)-1:
                print('************** Execute on the last queue RR Scheduling algorithm *************')
#print(q_list[i].process_list[])
# The last queue resets the arrival time 
            for t in range(len(q_list[i].process_list)):
                q_list[i].process_list[t].arrive_time=t
                rr_last_queue=RR(q_list[i].process_list,q_list[i].q)
                rr_last_queue.scheduling()
            else:
                currentQueue=q_list[i]
                index=int(0)
        while(True):
            if currentQueue.get(index).left_serve_time>q_list[i].q:
                currentQueue.get(index).left_serve_time-=q_list[i].q
                print(' The first %d Queue time slice : %d'%(i,q_list[i].q))
                print(' The process is not finished , Need to be added to the end of the next queue ： Process name ：%s '%(currentQueue.get(index).name))
# Throw the current process to the end of the next queue 
                q_list[i+1].add(currentQueue.get(index))
                index+=1
            else:
                print(' The service completes and pops up :',currentQueue.get(index).name)
                currentQueue.get(index).left_serve_time=0
                currentQueue.delete(index)
            if index==currentQueue.size():
                break
    person=init(11)      
    person=scheduling(22)
    print(person)
