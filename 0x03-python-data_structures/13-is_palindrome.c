#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head node
 * description: checks if a singly linked list is a palindrome
 * Return: success(1) failure(0)
*/


int is_palindrome(listint_t **head)
{
	listint_t *tmp_head;
	int num_nodes, idx, i, j;
	int *num_arr;

	/*You should consider checking is theres a circle in the linked list*/
	if (head == NULL || *head == NULL)
		return (1);

	tmp_head = *head;
	num_nodes = num_node(tmp_head);

	idx = 0;
	num_arr = malloc(sizeof(int) * num_nodes);

	if (num_arr == NULL)
		return (0);

	while (tmp_head != NULL)
	{
		num_arr[idx] = tmp_head->n;
		tmp_head = tmp_head->next;
		idx++;
	}
	for (i = 0, j = 1; i <= (num_nodes / 2); i++, j++)
	{
		if (num_arr[i] != num_arr[num_nodes - j])
		{
			free(num_arr);
			return (0);
		}
	}
	free(num_arr);
	return (1);
}


/**
 * num_node - gets the number of nodes in a linked list
 * @head: pointer to head node of a linked list
 * description: gets the number of nodes in a linked list
 * Return: failure(-1) success(number of nodes)
*/
int num_node(listint_t *head)
{
	int num_node;

	if (head == NULL)
		return (0);
	num_node = 0;
	while (head != NULL)
	{
		num_node++;
		head = head->next;
	}
	return (num_node);
}
