#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palidrome
 * @head: pointer to the head pointer to the list
 * Return: integer
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (0);
	}

	listint_t *slow;
	listint_t *fast;
	listint_t *prev;
	listint_t *curr;
       	listint_t *next;
	listint_t *left;
	listint_t *right;

	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	prev = NULL;
	curr = slow;
	next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	left = *head;
	right = prev;

	while (right != NULL)
	{
		if (left->n != right->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}

	return (1);
}
