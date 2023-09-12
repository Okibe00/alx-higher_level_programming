#include "lists.h"
/**
 *	is_palindrome - checks if a list is a palindrome
 *	@head: pointer to head node
 *	description: Checks if a linked list is a palindrome
 *	Return: 1 (yes) 0 (no)
 *
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *curr, *prev;

	if (head == NULL || *head == NULL)
		return (1);
	fast = *head;
	slow = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	fast = *head;
	prev = NULL;
	while (slow->next != NULL)
	{
		curr = slow;
		slow = slow->next;
		curr->next = prev;
		prev = curr;
	}
	slow->next = prev;
	while (fast != NULL && slow != NULL)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}
