#include <stdio.h>
#include <pthread.h>
void thread1(int id)
{
	int i,count=1;
	for (i=1;i<30;i++)	
	{
		printf("pthread1 %d %d\n",pthread_self(),count++);
		usleep(10000);
	}
}
void thread2(int id)
{
	int i,count=1;
	for (i=0;i<30;i++)	
	{
		printf("pthread2 %d %d\n",pthread_self(),count++);
		usleep(10000);
	}
}
int main(void)
{
	pthread_t id1,id2;
	int i,ret1,ret2;

	ret1=pthread_create(&id1,NULL,(void*)thread1,0);
       ret2=pthread_create(&id2,NULL,(void*)thread2,0);

	if (ret1!=0||ret2!=0)
	{
		printf("Create pthread error!\n");
		//exit(0);
	}
	pthread_join(id1,NULL);
	pthread_join(id2,NULL);
	return (0);
}
