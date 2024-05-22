import { render, screen } from '@testing-library/react';
import UserComponent from '../components/UserComponent';

test('renders users header', () => {
  render(<UserComponent />);
  const headerElement = screen.getByText(/Users/i);
  expect(headerElement).toBeInTheDocument();
});
