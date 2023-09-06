#include "lists.h"
/**
  * check_cycle - checks a linked list for cycles
  * @list: list
  * description: checks a list fr cycles
  * Return: 0(false) 1(true)
*/
int check_cycle(listint_t *list)
{
		listint_t *slow, *fast;

		if (list == NULL)
			return (0);
		slow = list;
		fast = list;

		while (slow != NULL && fast != NULL && fast->next != NULL)
		{
			slow = slow->next;
			fast = fast->next->next;
			if (slow == fast)
				return (1);
		}
		return (0);
}
